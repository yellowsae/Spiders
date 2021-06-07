# //div[@class="id_chapterRoot__3F-hU container"]//div/img/@src
# //ul[@class="home_listArea__B_AQX"]/li[1]/a[1]/@href

# 一套本子爬取
import requests
import os
from parsel import Selector
from fake_useragent import UserAgent
import time

def get_url(url):
    headers = {
        'User-Agent':UserAgent().chrome
    }
    ip = '127.0.0.1:10809'
    proxies = { 
        'http':'http://' + ip,
        'https':'https://' + ip
    }
    response = requests.get(url, headers=headers, proxies=proxies)
    if response.status_code == 200:
        response.encoding='utf-8'
        return response
    else:
        return None


def get_html(html):
    selector = Selector(html)
    test_url = selector.xpath('//ul[@class="home_listArea__B_AQX"]/li[1]/a[1]/@href').get()
    test_url = 'https://rouman5.com' + test_url
    # pages_url = [] 
    # for page in selector.xpath('//ul[@class="home_listArea__B_AQX"]/li[1]/a[1]/@href').get():
    #     pages_url.append('https://rouman5.com' + page)
    return  test_url

def parse(base_url):
    urls = []   # 章节url 
    # for url in base_url:
    html = get_url(base_url)
    selector = Selector(html.text)
    name = selector.xpath('//div[@class="row"]//div[2]/h5[1]/text()').get()
    for info_url in selector.xpath('//div[@class="bookid_chapterBox__CRrx9"]//a/@href').getall():
        urls.append('https://rouman5.com' + info_url)
    return urls,name

def get_content(url):
    # 获取章节里的图片
    imgs_urls = []
    # for url in urls:
    time.sleep(0.2)
    info = get_url(url)
    selector = Selector(info.text)
    title = selector.xpath('//div[@class="id_chapterRoot__3F-hU container"]/h3/text()').get()
    imgs = selector.xpath('//div[@class="id_chapterRoot__3F-hU container"]//div/img/@src').getall()
    return  imgs

# 保存
def save(name,imgs):
    if not os.path.exists('./Hanman/' + name + '/'):
        os.mkdir('./Hanman/' + name + '/' )
    for img_url in imgs:
        img_name = img_url.split('/')[-1]
        try:
            time.sleep(0.2)
            content = get_url(img_url)
            with open ('./Hanman/' + name + '/' + img_name , 'wb' ) as f:
                f.write(content.content)
                print('下载成功' + img_url)
        except:
            print('Error')

def main():
    url = 'https://rouman5.com/home'
    html = get_url(url)
    test_url  = get_html(html.text)
    urls,name = parse(test_url)
    for info_url in urls:
        imgs = get_content(info_url)
    # if not os.path.exists('./Hanman/' + name + '/'):
    #     os.mkdir('./Hanman/' + name + '/')
        save(name,imgs)
    

if __name__ == '__main__':
    main()