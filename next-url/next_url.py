from fake_useragent import UserAgent
import requests 
from parsel import Selector 
import os 

def get_url(url):
    headers = {
        'User-Agent':UserAgent().random
    }
    ip = '127.0.0.1:10809'
    proxies = {
        'http':'http://' + ip,
        'https':'https://' + ip
    }
    response = requests.get(url,headers=headers,proxies=proxies)
    if response.status_code == 200:
        response.encoding='utf-8'
        return response
    else:
        None
    
def get_html(html,url):
    selector = Selector(html)
    next_url = selector.xpath('//div[@id="pages"]//a[@class="a1"][2]/@href').get() 
    img_urls = selector.xpath('//div[@class="content"]/img/@src').getall()
    title = selector.xpath('//div[@class="content"]/img/@alt').get()
    return next_url,img_urls

def parse(data,name,title):
    if not os.path.exists('./下一页url/' + title + '/'):
        os.mkdir('./下一页url/' + title + '/')
    with open('./下一页url/'+ title + '/' + name , 'wb') as f:
        f.write(data)
        print('保存成功')

def main(url,title):
    # url = 'https://www.tujigu.com/a/41553/'
    base_url = [] 
    base_url.append(url)
    cont = 1  # 索引 
    # 使用 While 循环，进行下一页的爬取 
    while url:
        html = get_url(url)
        url, img_urls = get_html(html.text,url)
        base_url.append(url)

        # 数据下载保存 
        for info_url in img_urls:
            data = get_url(info_url)
            name = info_url.split('/')[-1]
            parse(data.content,name,title)
        cont +=1 
        # 判断是否相同，如果相同就停止循环 
        if base_url[cont-2] == base_url[cont-1]:
            # 删除最后一个元素，因为最后一个是重复的
            base_url.pop() 
            break

def start_urls(html):
    selector = Selector(html)
    base_url = selector.xpath('//div[@class="hezi"]//li/a/@href').getall()
    titles = selector.xpath('//ul[@class="img"]//p/a/text()').getall()
    return base_url,titles

if __name__ == '__main__':
    url = 'https://www.tujigu.com/search/%E6%9D%A8%E6%99%A8%E6%99%A8'
    html = get_url(url)
    base_url,titles = start_urls(html.text)
    # 爬取多套套图 , title 套图名字 
    for info_url,title in zip(base_url,titles):
        main(info_url,title)