import requests 
import os 
from fake_useragent import UserAgent
from parsel import Selector
import time 

if not os.path.exists('./壁纸项目/Img/'):
    os.mkdir('./壁纸项目/Img/')


def get_url(url):
    headers = {
        'User-Agent':UserAgent().chrome
    }
    ip = '127.0.0.1:10809'
    proxies = {
        'http':'http://'+ ip ,
        'https':'https://' + ip 
    }
    response = requests.get(url,headers=headers,proxies=proxies)
    if response.status_code == 200:
        return response
    else:
        return None

def get_html(html):
    selector = Selector(html)
    info_url = [] 
    for url in selector.xpath('//ul[@id="post-list-posts"]/li//a[@class="thumb"]/@href').getall():
        info_url.append('https://konachan.net' + url )
    return info_url

def parse(html):
    selector = Selector(html)
    img_url = selector.xpath('//div[@class="content"]//img/@src').get()
    return img_url 


def save(img_url):
    try:
        cont = get_url(img_url)
        name = img_url.split('/')[-1]
        with open('./壁纸项目/Img/' + name , 'wb') as f :
            f.write(cont.content)
            print('保存成功')
    except:
        print('eee')
        pass

def main():
    for page in range(1,10+1):
        url = f'https://konachan.net/post?page={page}&tags=' 
        html = get_url(url)
        base_url = get_html(html.text)
        for info_url in base_url:
            html = get_url(info_url)
            img_url  = parse(html.text)
            save(img_url)

if __name__ == '__main__':
    main()