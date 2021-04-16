from fake_useragent import UserAgent
from parsel import Selector
import os 
import requests
from time import sleep

if not os.path.exists('./XianNvTu/Img'):
    os.mkdir('./XianNvTu/Img')

# 发送请求
def get_url(url):
    headers = {
        'User-Agent':UserAgent().random
    }
    ip = '127.0.0.1:10809'
    proxies = {
        'http':'http://'+ ip,
        'https':'https://' + ip
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        response.encoding='utf-8'
        return response
    else:
        return None

# 图片解析 
def parse(html):
    selector = Selector(html)
    urls = selector.xpath('//div[@class="content"]//img/@src').getall()
    title = selector.xpath('//h1/text()').get()
    return urls, title


# 解析获取下一页的url 
def get_html(html):
    selector = Selector(html)
    next_url = selector.xpath('//div[@id="pages"]//a[@class="a1"][3]/@href').get()
    return next_url

# 获取所有页面的url 
def parse_all_urls(url):
    base_url = [] 
    base_url.append(url)
    cout = 1
    while url:
        html = get_url(url)
        url = get_html(html.text)
        base_url.append(url)
        cout +=1 
        if base_url[cout - 2 ] == base_url[cout - 1]:
            base_url.pop()
            break
    return base_url 

# 数据保存 
def save(img_url,title):
    for url in img_url:
        try:
            name = url.split('/')[-1]
            # 这里访问不了， 404 ， 服务器不给爬 
            content = get_url(url)
            if not os.path.exists('./XianNvTu/Img/' + title + '/'):
                os.mkdir('./XianNvTu/Img/' + title + '/')
            with open('./XianNvTu/Img/ ' + title + '/' + name, 'wb') as f:
                f.write(content.content)
                print('保存成功', title, name)
        except:
            pass
        
def start_url(url):
    html = get_url(url)
    selector = Selector(html.text)
    urls = selector.xpath('//ul[@class="img"]/li/a/@href').getall()
    # titles = selector.xpath('//ul[@class="img"]/li/p[@class="p_title"]/a/text()').getall()
    return urls

def main():
    url = 'http://www.xiannvku.com/index.php/pic/search'
    urls = start_url(url)
    for url in urls:
        base_url = parse_all_urls(url)
        for info_url in base_url:
            html = get_url(info_url)
            img_url, title = parse(html.text)
            save(img_url,title)

    # url = 'http://www.xiannvku.com/pic/show-13933-1.html'
    # base_url = parse_all_urls(url)

if __name__ == '__main__':
    main()