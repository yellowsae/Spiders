import requests
import os
import csv
import parsel
import ssl

# 加上ssl 证书
ssl._create_default_https_context = ssl._create_unverified_context

# 因为服务器对爬虫得限制，返回不到内容

def get_url(url):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    html_date = response.text
    selector = parsel.Selector(html_date)
    lis = selector.xpath('//div[@class="board-item-main"]')
    for li in lis:
        name = li.xpath('.//p[@class="name"]/a/@title').get() # 电影名字
        attor = li.xpath('.//p[@class="star"]/text()').get().strip()
        Up_time = li.xpath('.//p[@class="releasetime"]/text()').get()
        score = li.xpath('.//p[@class="score"]/i[1]/text()').get() + li.xpath(
            './/p[@class="score"]/i[2]/text()').get()
        print(name, attor, Up_time, score, sep=(' | '))
        # if not os.path.exists('./maoyan2.csv'):
        #     os.mkdir('./maoyan.csv')
        # with open('./maoyan.csv', 'a') as f:
        #     write = csv.writer(f)
        #     write.writerow([name, attor, Up_time, score])


url = 'https://maoyan.com/board/4?offset=0'
get_url(url)
