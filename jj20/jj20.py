#!/bin/python3.9

import requests
import parsel
import os
# 多线程
import threading


def get_url(url):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    html_date = response.text
    selector = parsel.Selector(html_date)
    lis = selector.xpath('//ul[@class="picbz"]/li')
    for li in lis:
        page_url = 'http://www.jj20.com' + li.xpath(
            './a/@href').get() # 进行对详情页的拼接
        page_title = li.xpath('./a[2]/text()').get()
        # print(page_url, page_title)
        # 主页  http://www.jj20.com/bz/ktmh/list_16_cc_13_1.html
        # 详情页 http://www.jj20.com/bz/ktmh/dmrw/298030.html
        res = requests.get(url=page_url, headers=headers).text
        sele = parsel.Selector(res)
        # 使用css 选择器获取 src 中的链接，使用了 attr()方法
        # lis_2 = sele.css(
        #     '#showImg li img::attr(src)').getall() # getall()  返回的是 list
        # 使用xpath 获取 img -> src 中的链接
        # lis_2 = sele.xpath(
        #     '//ul[@class="fix"]/li/img/@src').getall() # 一般是保存为 list 类型 好 操作
        # 这里使用xpath 只能获取每一页的第一张图，跳转不到第二张 ?
        # 已解决，--> 直接复制浏览器中的xpath。然后进行修改，到能获取的目标就行
        lis_2 = sele.xpath('//*[@class="fix"]//img/@src').getall()
        for i, li_2 in enumerate(lis_2):
            # li_2 是缩略图
            #原图   http://cj.jj20.com/up/allimg/1114/0112211AK6/2101121AK6-1.jpg
            #       http://img.jj20.com/up/allimg/1114/0112211AK6/2101121AK6-1.jpg
            #       http://pic.jj20.com/up/allimg/1114/0112211AK6/2101121AK6-1.jpg
            #缩略图 http://img.jj20.com/up/allimg/1114/0112211AK6/2101121AK6-1-lp.jpg
            img_url = li_2.replace('-lp.jpg', '.jpg') # 原图, 只需要改这个就行了
            img_title = page_title + str(i) + os.path.splitext(img_url)[
                -1] #名字加1
            #对字符串的操作方法有很多
            # img_title = page_title + img_url.split('-')[
            #     -1] # 以 - 进行分割，然后取[-1]，的字符串

            # 使用enumerate()是从0开始，使用.split()进行分割获取，更好，更准确
            print(img_url, img_title)

            # 下载保存
            # if not os.path.exists('./ACG_img/'):
            #     os.mkdir('./ACG_img/')
            # path = './ACG_img/' + img_title # 图片命名
            # img_url_response = requests.get(url=img_url, headers=headers)
            # try:
            #     with open(path, mode='wb') as f:
            #         f.write(img_url_response.content)
            # except:
            #     pass
            # print("下载成功==", img_url, img_title)


if __name__ == "__main__":
    url = 'http://www.jj20.com/bz/ktmh/list_16_cc_13_1.html'
    get_url(url)
