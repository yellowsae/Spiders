from fake_useragent import UserAgent
import requests 
from parsel import Selector
import os 
from time import sleep

if not os.path.exists('./n-hentai/Img/'):
    os.mkdir('./n-hentai/Img/')

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
        return response
    else:
        return None


def get_html(html):
    selector = Selector(html)
    # 爬不了 
    img_all = selector.xpath('//div[@class="thumb-container"]//a/img/@data-src').getall()
    # img_all = selector.css('').getall()
    img_name = selector.xpath('//div[@id="info"]//h2/text()').get()
    return img_all , img_name

# save 
def img_contents(img_all,title):
    for url in img_all:
        content =  get_url(url)
        img_name = url.split('/')[-1]
        with open('./n-hentai/Img/' + title + img_name ,'wb') as f : 
            f.write(content.content)
            print('下载成功',img_name)

def main(base_url):
    # url = 'https://nhentai.to/g/340551'
    for url in base_url:
        html = get_url(url)
        img_all,img_name = get_html(html.text)
        img_contents(img_all,img_name)

# 多个本子url 
def get_info_img(html):
    selector = Selector(html)
    base_url = [] 
    info_url = selector.xpath('//div[@class="gallery"]/a/@href').getall()
    [ base_url.append("https://nhentai.to" + url) for url in info_url ]
    return base_url

if __name__ == '__main__':
    # 没有进行页面循环 
    url = 'https://nhentai.to/search?q=asanagi&page=1'
    html = get_url(url)
    base_url = get_info_img(html.text)
    main(base_url)

# 