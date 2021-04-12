import requests
from parsel import Selector 
from time import sleep 
import os 
from fake_useragent import UserAgent 

def get_url(url):
    headers = {
        'User-Agent':UserAgent().random
    }
    ip = '127.0.0.1:10809'
    proxies = { 
        'http':'http://'+ip,
        'https':'https://'+ip
    }
    response = requests.get(url,headers=headers,proxies=proxies)
    if response.status_code == 200:
        return response
    else:
        return None

def get_html(html):
    selector = Selector(html)
    base_url = selector.xpath('//div[@class="thumbnail-container"]//a/@href').getall()
    return base_url

def parse(html):
    selector = Selector(html)
    img_url = selector.xpath('//img[@id="image"]/@src').get()
    name = img_url.split('/')[-1]
    return img_url,name

def save(datas,name):
    if not os.path.exists('./Gelbooru/Img/'):
        os.mkdir('./Gelbooru/Img')
    with open('./Gelbooru/Img/' + name, 'wb') as f:
        f.write(datas)
        print('保存成功')

def main():
    # 爬取10页 
    for page in range(0,11):
        url = f'https://gelbooru.com/index.php?page=post&s=list&tags=emilia_%28re%3Azero%29&pid={page * 42}'
        html = get_url(url)
        base_url = get_html(html.text)
        for info_url in base_url:
            html = get_url(info_url)
            img_url,name = parse(html.text)
            con = get_url(img_url)
            save(con.content,name)


# def page():
#     for page in range(0,11):
#         url = f'https://gelbooru.com/index.php?page=post&s=list&tags=emilia_%28re%3Azero%29&pid={page * 42}'
#         print(url)

if __name__ == '__main__':
    main()
    # page()