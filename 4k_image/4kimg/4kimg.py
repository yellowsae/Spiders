from fake_useragent import UserAgent
from parsel import Selector
from time import sleep
import os 
import requests 

def get_url(url):
    headers = {
        'User-Agent':UserAgent().random
    }
    ip = '127.0.0.1:10809'
    proxies = {
        'http':'http://'+ip,
        'https':'https://' + ip 
    }
    sleep(0.5)   # 休眠 
    response = requests.get(url,headers=headers,proxies=proxies)
    if response.status_code == 200:
        response.encoding='utf-8'
        return response
    else:
        return None

def get_html(html):
    selector = Selector(html)
    base_url = [] 
    for url in selector.xpath('//div[@class="slist"]/ul/li/a/@href').getall():
        base_url.append('https://pic.netbian.com' + url)
    return base_url

def parse(html):
    selector = Selector(html)
    cont = selector.xpath('//div[@class="photo-pic"]//a/img/@src').get()
    img_url = 'https://pic.netbian.com' + cont
    return img_url

def save(img_url):
    if not os.path.exists('./壁纸项目/Img/'):
        os.mkdir('./壁纸项目/Img/')
    try:
        cont = get_url(img_url)
        name = img_url.split('/')[-1]
        with open('./壁纸项目/Img/' + name , 'wb') as f:
            f.write(cont.content)
            print('sssss')
    except:
        print('eeee')
        pass
def main():
    for page in range(21):
        url = f'https://pic.netbian.com/4kdongman/index_{page}.html'
        html = get_url(url)
        base_url = get_html(html.text)
        for info in base_url:
            html = get_url(info)
            img_url = parse(html.text)
            save(img_url)


if __name__ == '__main__':
    main()