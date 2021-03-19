# 爬取 网盘链接
import os
import ssl
import requests
import parsel
import csv
# ssl.ALERT_DESCRIPTION_ACCESS_DENIED
for pape in range(12540, 12583, 1):
    url = f'http://bbs.zzbaorui.com/show.asp?id={pape}'
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    response.encoding = "gb18030"
    res = response.text
    selector = parsel.Selector(res)

    lis = selector.xpath('//div[@class="pull-left wrap-left"]')
    # //div[@class="pull-left wrap-left"]//div[@class="art-ctt-iframe"]/div[@class="article-content-wrap"]/p/span/text()
    for div in lis:

        img = div.xpath(
            './/div[@class="art-ctt-iframe"]/div[@class="article-content-wrap"]/p[1]/img'
        ).get()
        img3 = div.xpath(
            './/div[@class="art-ctt-iframe"]/div[@class="article-content-wrap"]/p[3]/img'
        ).get()
        name = div.xpath(
            './/div[@class="art-ctt-iframe"]/div[@class="article-content-wrap"]/p[5]/span/text()'
        ).get()

        big = div.xpath(
            './/div[@class="art-ctt-iframe"]/div[@class="article-content-wrap"]/p[6]/span/text()'
        ).get()

        mmk = div.xpath(
            './/div[@class="art-ctt-iframe"]/div[@class="article-content-wrap"]/p[7]/span/text()'
        ).get()

        uul = div.xpath(
            './/div[@class="art-ctt-iframe"]/div[@class="article-content-wrap"]/p[9]/span[2]/text()'
        ).get()

        pa = div.xpath(
            './/div[@class="art-ctt-iframe"]/div[@class="article-content-wrap"]/p[8]/span[2]/text()'
        ).get()
        print(name, big, mmk, uul, pa, sep=" | ")
        # with open('~/py/img.jpg', mode='wb') as f:
        #     f.write(img)
        #     f.write(img3)
        pass
