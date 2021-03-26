from fake_useragent import UserAgent
from parsel import Selector
import requests
import os 

if not os.path.exists('./xiuren/YCC/'):
    os.mkdir('./xiuren/YCC')

def get_url(url):
    headers = {
        'User-Agent':UserAgent().random
    }
    proxy = '127.0.0.1:10809'
    proxies = {
        'http':'http://' + proxy,
        'https':'https://' + proxy
    }
    response  = requests.get(url,headers=headers,proxies=proxies)
    if response.status_code == 200:
        return response
    else:
        return None

def get_html(html):
    selector = Selector(html)
    all_url = selector.xpath('//div[@class="photos"]/a/div/@src').getall()
    title = selector.xpath('//h1/text()').get()
    base_url = [] 
    for url in all_url:
        base_url.append('https://xchina.co' + url)
    return base_url ,title

def save_data(img_url,title):
    if not os.path.exists('./xiuren/YCC/' + title + '/'):
        os.mkdir('./xiuren/YCC/' + title + '/')
    for url in img_url:
        img_info = get_url(url)
        name = url.split('/')[-1]
        with open('./xiuren/YCC/' + title + '/' + name , 'wb' ) as f :
            f.write(img_info.content)
            print('下载成功',url)

def main():
    for page in range(1,8):
        url = f'https://xchina.co/photo/id-5f3901468ae5d/{page}.html'
        html = get_url(url)
        base_url ,title = get_html(html.text)
        save_data(base_url,title)
if __name__ == '__main__':
    main()



# 爬取单个 ， 在for 循环里改变爬取的url 

# url = 'https://xchina.co/photos/model-%E6%9D%A8%E6%99%A8%E6%99%A8sugar.html'
