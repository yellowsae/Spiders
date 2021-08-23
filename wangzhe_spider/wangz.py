import requests
import parsel
import time
import re

data = []


def get_info(html_date):
    lis = html_date.xpath(
        '//ul[@class="herolist clearfix"]/li/a/@href').getall()
    for li in lis:
        hero_url = 'https://pvp.qq.com/web201605/' + li
        data.append(hero_url)


def get_url(url):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return parsel.Selector(response.text)
    return None


def get_img_url():
    for url1 in data:
        sele = get_url(url1)
        img_url = sele.xpath('//div[@class="zk-con1 zk-con"]/@style').get()
        result = re.match('^background:\surl(.*?)\scenter\s0px$',
                          img_url) # 他妈的正则


if __name__ == "__main__":
    url = 'https://pvp.qq.com/web201605/herolist.shtml'
    html = get_url(url)
    get_info(html)
    get_img_url()
