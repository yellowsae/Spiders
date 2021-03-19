#!/bin/python3.9

import requests
import parsel
import os
import time
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
        # 使用 css 获取 img -> src 中的链接
        # lis_2 = sele.css(
        #     '#showImg li img::attr(src)').getall() # getall()  返回的是 list
        # 使用xpath 获取 img -> src 中的链接
        # lis_2 = sele.xpath('//ul[@class="fix"]/li/img/@src').getall()  # 一般是保存为 list 类型 好 操作, 这个用不了
        lis_2 = sele.xpath(
            '//*[@class="fix"]//img/@src').getall() # 这个xpath 可以用
        # print(type(lis_2))

        for i, li_2 in enumerate(lis_2):
            # li_2 是缩略图
            #原图   http://cj.jj20.com/up/allimg/1114/0112211AK6/2101121AK6-1.jpg
            #       http://img.jj20.com/up/allimg/1114/0112211AK6/2101121AK6-1.jpg
            #       http://pic.jj20.com/up/allimg/1114/0112211AK6/2101121AK6-1.jpg
            #缩略图 http://img.jj20.com/up/allimg/1114/0112211AK6/2101121AK6-1-lp.jpg
            img_url = li_2.replace('-lp.jpg', '.jpg') # 原图, 只需要改这个就行了
            img_title = page_title + str(i) + os.path.splitext(img_url)[-1]
            print(img_url, img_title)
            #
            # 下载保存
            if not os.path.exists('./ACG_img/'):
                os.mkdir('./ACG_img/')
            path = './ACG_img/' + img_title # 图片命名
            img_url_response = requests.get(url=img_url, headers=headers)
            try:
                with open(path, mode='wb') as f:
                    f.write(img_url_response.content)
                    pass
            except:
                pass
            print("下载成功==", img_url, img_title)


if __name__ == "__main__":
    # 计算时间
    start_time = time.time()
    # 翻页
    for page in range(1, 24):
        # 这个url 还可以改， 在13这个位置, 不同类型而已
        url = 'http://www.jj20.com/bz/ktmh/list_16_cc_13_{}.html'.format(page)
        threading.main_thread = threading.Thread(target=get_url, args=(url, ))
        threading.main_thread.start()
        # get_url(url) print("程序需要时间:", time.time() - start_time)
