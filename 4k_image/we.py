from fake_useragent import UserAgent
import requests 
from parsel import Selector
import os 
from time import sleep

if not os.path.exists('./壁纸项目/Img/'):
    os.mkdir('./壁纸项目/Img/')

def get_url(url):
    proxy = '127.0.0.1:10809'
    proxies = {
        'http':'http://' + proxy,
        'https' : 'https://' + proxy
    }
    headers= {
        'User-Agent':UserAgent().chrome
    }
    sleep(0.2)
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        response.encoding='utf-8'
        return response
    else:
        return None


def get_html(html):
    selector = Selector(html)
    netx_url = selector.xpath('//ul[@class="wallpapers__list"]//li/a/@href').getall()   # 获取不了url 
    base_url = [] 
    for url in netx_url:
        netx_url = 'https://wallpaperscraft.com' + url 
    return base_url


def parse(html):
    selector = Selector(html)
    img_url = selector.xpath('//div[@class="wallpaper"]//img/@src').get()
    return img_url



def save(img_url):
    try:
        cont = get_url(img_url)
        name = img_url.split('/')[-1]
        with open ('./壁纸项目/Img' + name , 'wb') as f :
            f.write(cont.content)
            print('suefff')
    except:
        print('eee')
        pass

def main():
    url = 'https://wallpaperscraft.com/catalog/anime/'
    html = get_url(url)
    base_url = get_html(html.text)
    for info_url in base_url:
        html = get_url(info_url)
        img_url = parse(html.text)
        save(img_url)

if __name__ == '__main__':
    main()