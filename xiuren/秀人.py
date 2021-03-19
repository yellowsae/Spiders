import requests
import parsel
import time
import os
import urllib.request

img_url = []

if not os.path.exists('./xiuren/'):
    os.mkdir('./xiuren/')


def spider(list_url, title):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    for url, titles in zip(list_url, title):
        html = get_url(url)
        proxy = '127.0.0.1:1080'
        proxies = {'http': 'socks5://' + proxy, 'https': 'socks5://' + proxy}
        selector = parsel.Selector(html)
        # <<<<<<< HEAD
        img_url.append(
            selector.xpath('//ul[@id="hgallery"]/img/@src').getall())
        for i, img_list in enumerate(img_url):
            for url1 in img_list:
                response = requests.get(url=url1,
                                        headers=headers,
                                        proxies=proxies)
                try:
                    with open('./xiuren/' + title[i] + str(i) + '.jpg',
                              'wb') as f:
                        f.write(response.content)
                        print("下载成功", url, title[i])
                except:
                    print("error")


# =======
#         img_url.append(selector.xpath('//ul[@id="hgallery"]/img/@src').getall())
#         for i , img_list in enumerate(img_url):
#             for url1 in img_list:
#                 print(url1)
# res = requests.get(url=url1,headers=headers)
#         try:
#             with open('./xiuren/' + title[i] + os.path.splitext(img_url)[-1] , 'wb' ) as f :
#                 f.write(response.content)
#                 print("下载成功",url,title[i])
#         except :
#             pass
# # [  print (url) for url in img_list for img_list in img_url]
# for imgs in selector.xpath('//ul[@id="hgallery"]'):
#     img_url = imgs.xpath('.img/@src').getall()
#     print(img_url)
# >>>>>>> b50b4d6 (2021-02-21)

# [  print (url) for url in img_list for img_list in img_url]
# for imgs in selector.xpath('//ul[@id="hgallery"]'):
#     img_url = imgs.xpath('.img/@src').getall()
#     print(img_url)


def get_content(html):
    selector = parsel.Selector(html)
    link = "https://www.nvshens.org"
    url_list = []
    title = []
    for li in selector.xpath('//li[@class="igalleryli"]'):
        url_list.append(link + li.xpath('.//a/@href').get())
        title.append(li.xpath(".//img/@title").get())
    return url_list, title


def get_url(url):
    time.sleep(1)
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = response.apparent_encoding # 防止乱码
        return response.text
    return 'ERROR'


def main():
    url = "https://www.nvshens.org/girl/22162/album/1.html"
    html = get_url(url)
    list_url, title = get_content(html)
    spider(list_url, title)


if __name__ == "__main__":
    main()
