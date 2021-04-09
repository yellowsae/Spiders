from fake_useragent import UserAgent
import requests 
from parsel import Selector
from time import sleep
import os 

def get_url(url):
    headers = {
        "User-Agent":UserAgent().random
    }
    response =requests.get(url,headers=headers)
    if response.status_code == 200:
        response.encoding='gbk'
        return response
    else:
        return None


def get_html(html):
    selector = Selector(html)
    img_url = selector.xpath('//tr[1]//div[@class="page"][1]/a/@href').getall()
    # tbody 爬不了 ， 把tbody 去掉就能爬 
    # img_url = selector.xpath('//tbody/tr[2]/td/div[@class="page"]/a/@href').getall()
    base_url = [] 
    for img in img_url:
        base_url.append('https://www.xiurenji.cc' + img)
    base_url.pop() # 删掉最后一个 
    return base_url

def get_info(img_info):
    selector = Selector(img_info)
    urls = selector.xpath('//div[@class="img"]//img/@src').getall()
    img_url = [] 
    for url in urls:
        img_url.append('https://xr.plmn5.com' + url)
    title = selector.xpath('//div[@class="img"]//img[1]/@alt').get()
    return img_url,title

def save_data(img_url,title):
    if not os.path.exists('./xiuren/YCC/' + title):
        os.mkdir('./xiuren/YCC/' + title)
    for i,url in  enumerate(img_url):
        info = get_url(url)
        name = url.split('/')[-1]

        with open('./xiuren/YCC/' + title + '/' + str(i) + name , 'wb') as f:
            f.write(info.content)
            print('保存成功', title)

# 这里获取单次套图， 之后循环爬取就行了 
def main(urls):
    # url = 'https://www.xiurenji.cc/XiuRen/7883.html'
    for url in urls:
        html = get_url(url)
        img_all_url = get_html(html.text)
        for url in img_all_url:
            img_info = get_url(url)
            img_url , title = get_info(img_info.text)
            save_data(img_url,title)

def all_img(url):
    html = get_url(url)
    selector = Selector(html.text)
    urls = selector.xpath('//div[@class="title1"]//a/@href').getall()
    base_url = [] 
    for url in urls:
        base_url.append('https://www.xiurenji.cc' + url)
    return base_url

if __name__ == "__main__":
    # 开始 
    for page in range(1,32):
        url = f'https://www.xiurenji.cc/plus/search/index.asp?keyword=%D1%EE%B3%BF%B3%BF&searchtype=title&p={page}'
        base_url = all_img(url)
        main(base_url)