from fake_useragent import UserAgent
import requests 
import os 
from parsel import Selector
from time import sleep

if not os.path.exists('./e-hentai/Img/'):
    os.mkdir('./e-hentai/Img/')

def get_url(url):
    heasers = {
        "User-Agent":UserAgent().chrome
    }
    proxy = '127.0.0.1:10809'
    proxies = {
        'http':'http://' + proxy,
        'https':'https://' + proxy
    }
    response = requests.get(url,headers=heasers,proxies=proxies)
    if response.status_code == 200:
        return response
    else:
        return None

def get_html(html):
    selector = Selector(html)
    img_all_url = selector.xpath('//div[@id="gdt"]/div//a/@href').getall()  # list 
    return img_all_url


def get_info(info):
    selector = Selector(info)
    img_url = selector.xpath('//div[@id="i3"]//img/@src').get()
    img_name = img_url.split('/')[-1]
    content = get_url(img_url)
    with open ('./e-hentai/Img/' + img_name , 'wb' ) as f :
        f.write(content.content)
        print('下载成功',img_url)
    


def main():
    url = 'https://e-hentai.org/g/1869046/638fba71b5/'
    html = get_url(url)
    all_url = get_html(html.text)
    for img_url in all_url:
        info = get_url(img_url)
        get_info(info.text)

if __name__ == '__main__':
    main()