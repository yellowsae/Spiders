from fake_useragent import UserAgent
import requests 
from parsel import Selector
import os 
from time import sleep

if not os.path.exists('./24mn/Img/'):
    os.mkdir('./24mn/Img/')

def get_url(url):
    proxy = '127.0.0.1:10809'
    proxies = {
        'http':'http://' + proxy,
        'https' : 'https://' + proxy
    }
    headers= {
        'User-Agent':UserAgent().chrome
    }
    response = requests.get(url,headers=headers,proxies=proxies)
    if response.status_code == 200:
        response.encoding='utf-8'
        return response
    else:
        return None


def get_html(html):
    selector = Selector(html)
    netx_url = selector.xpath('//div[@class="page ps"]/a[7]/@href').get()
    netx_url = 'https://www.24tupian.org' + netx_url
    return netx_url



def Img_parse(html):
    selector = Selector(html)
    img_url = selector.xpath('//div[@id="imgshow"]/a/img/@src').get()
    return img_url


def parse(html):
    selector = Selector(html)
    title = selector.xpath('//h1/text()').get()
    # url = selector.xpath('//div[@class="gtps fl"]//li/a/@href').getall()
    base_url = [] 
    for url in selector.xpath('//div[@class="gtps fl"]//li/a/@href').getall():
        base_url.append('https://www.24tupian.org' + url)

    img_urls = []
    for info_url in base_url:
        html = get_url(info_url)
        url = Img_parse(html.text)
        img_urls.append(url)
    # 全部的img_url
    return img_urls,title

# 获取所有页面的url 
def Info_url(url):
    base_url = [] 
    base_url.append(url)
    cout = 1
    while url:
        html = get_url(url)
        url = get_html(html.text)
        base_url.append(url)
        cout +=1 
        # 下一页判断
        if base_url [ cout - 1 ] == 'https://www.24tupian.orgjavascript:void(0)':
            base_url.pop()
            break

        # 一般的爬取下一页 
        # if base_url[cout - 2 ] == base_url[cout - 1]:
        #     base_url.pop()
        #     break
    return base_url 

def save(img_urls,title):
    if not os.path.exists('./24mn/Img/' + title + '/'):
        os.mkdir('./24mn/Img/' + title + '/')
    try:
        for img_url in img_urls:
            name = img_url.split('/')[-1]
            cont = get_url(img_url)
            with open ('./24mn/Img/' + title + '/' + name , 'wb') as f :
                f.write(cont.content)
                print('下载成功',title,name)
    except:
        print('Error')
        pass

def All_url(url):
    html = get_url(url)
    selector = Selector(html.text)
    urls = [] 
    for url in selector.xpath('//div[@class="paihan fl"]//li/a/@href').getall():
        urls.append( 'https://www.24tupian.org' + url)
    return urls

def main():
    for page in range(1,11):
        url = f'https://www.24tupian.org/model/yangchenchensugar_{page}.html'
        urls = All_url(url)    
        # url = 'https://www.24tupian.org/hd2/tuimo46192.html'
        for url in urls:
            base_url = Info_url(url)
            for info_url in base_url:
                html = get_url(info_url)
                img_urls,title = parse(html.text)
                save(img_urls,title)

if __name__ == '__main__':
    main()