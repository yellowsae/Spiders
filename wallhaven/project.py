# 小爬虫，壁纸项目 

from  fake_useragent import UserAgent
import  os
from parsel import Selector
import  requests


def get_url (url):
    ip = "127.0.0.1:10809"
    proxies = {
        "http": "http://" + ip,
        "https": "https://" + ip
    }
    headers = {
        "User-Agent": UserAgent().random
    }
    response  = requests.get(url, headers=headers, proxies= proxies)
    if (response.status_code == 200):
        return response
    else:
        return None

# https://th.wallhaven.cc/small/e7/e7ek7k.jpg  
# https://w.wallhaven.cc/full/e7/wallhaven-e7ek7k.jpg
# href  :  https://wallhaven.cc/w/e7ek7k



def get_html(html):
    selector = Selector(html.text)
    # 详情页面 ： //section[@class="thumb-listing-page"]//ul/li//a/@href 
    info_url = selector.xpath("//section[@class='thumb-listing-page']//ul/li//a/@href").getall()
    for url in info_url:  # 循环所有详情页
        info_html = get_url(url)
        Spiders(info_html)



def Spiders(info_html):
    selector = Selector(info_html.text)
    # img_url的解析：  //div[@class="scrollbox"]//img/@src
    img_url = selector.xpath('//div[@class="scrollbox"]//img/@src').get()
    save(img_url)


def save(img_url):
    if not os.path.exists("./Img/"):
        os.mkdir("./Img/")

    try: 
        content_img = get_url(img_url)
        name = img_url.split('/')[-1]
        with open("./Img/" + name, "wb") as f:
            f.write(content_img.content)
            print("下载成功" + " " + img_url)

    except :
        print("error" + img_url)
        pass




def main():
    url = 'https://wallhaven.cc/toplist?page=2'
    html = get_url(url)
    get_html(html)



if __name__ == '__main__':
    main()

