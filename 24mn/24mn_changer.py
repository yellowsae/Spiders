from fake_useragent import UserAgent
import requests 
from parsel import Selector
import os 
from time import sleep

def get_url(url):
    proxy = '127.0.0.1:10809'
    proxies = {
        "http": "http://" + proxy,
        "https": "https://" + proxy
    }
    headers = {
        "User-Agent": UserAgent().random,
    }
    # 发送请求 
    response = requests.get(url=url, headers=headers)
    if ( response.status_code == 200):
        response.encoding = "utf-8"
        return response
    else:
        return None
# https://big.diercun.com/hd2/2021/0901/30/24mnorg_1%201.jpg
# https://big.diercun.com/hd2/2021/0901/30/m24mnorg_1%201.jpg

def get_html(html,url):  # 解析html 获取到 下一页的url 
    selector = Selector(html.text)
    next_all = selector.xpath('//div[@class="page ps"]/a/@href').getall()

    # 处理数组数据
    next_url = set(next_all)
    next_url.remove("javascript:void(0)")
    url_all = []
    url_all.append(url) 
    for url in next_url:
        url_all.append('https://www.24tupian.org' + url)
    return url_all


def SpidersImg(next_urls):
    # 循环爬取
    for url in next_urls:
        response = get_url(url)
        selector = Selector(response.text)
        img_big = []
        img_src = selector.xpath('//div[@class="gtps fl"]//img/@src').getall() # img_url
        title = selector.xpath('//h1/text()').get()  # 文件夹
        for info_url in img_src:
            # 处理url
            newstr = list(info_url)
            newstr[42] = ""
            info_url = "".join(newstr)
            img_big.append(info_url.replace("imgs","big"))
        save(img_big, title)

def save(img_big,title):
    img_path = "./24mn/Img/" + title + "/"
    if not os.path.exists(img_path):
        os.mkdir(img_path)
    try: 
        for src in img_big:
            sleep(0.3)
            name = src.split("/")[-1]
            img_content = get_url(src)
            with open(img_path + name , "wb") as f:
                f.write(img_content.content)
                print("下载成功" + " " + src)
    except:
        print ("Error saving")
        


def main():
    url = 'https://www.24tupian.org/hd2/tuimo47956.html'
    html = get_url(url)
    next_urls = get_html(html,url)
    SpidersImg(next_urls)

if __name__ == '__main__':
    main()