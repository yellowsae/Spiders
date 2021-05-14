import requests
from fake_useragent import UserAgent
from time import sleep
import os
from parsel import Selector
from jsonpath import jsonpath


def get_url(url):
    headers = {
        'User-Agent':UserAgent().chrome
    }
    ip = '127.0.0.1:10809'
    proxies = {
        'http':'http://'+ ip,
        'https':'https://' + ip
    }
    response = requests.get(url,headers=headers,proxies=proxies)
    if response.status_code == 200:
        return response
    else:
        return response


def get_html(html):
    # title_top = jsonpath(html,'$..title')
    contents = [] 
    base = jsonpath(html,'.')[0]    # 主循环 
    for info in base:
        item = {}
        item['title_cd'] = info['title']
        contents = info['content']  # 这里直接用来循环 ， 不用 [] ____ 

        for con in contents:
            item['title'] = con['title']
            # item['p'] = con['p']  # 这里找不到 
            item['cd_title'] = con['cd_title']
            item['time'] = con['time']
            contents.append(item)
            print(item)    
    return contents
    # title = jsonpath(html,'$..content..title')
    # p = jsonpath(html,'$..content..p')
    # cd_title = jsonpath(html,'$..content..cd_title')
    # time = jsonpath(html,'$..content..time')
    # # print(title_top)
    # print(title_top,title,p,cd_title,time)

def main():
    url = 'https://player.vcollection.org/data/result.json?1260179027'
    html = get_url(url)
    contents = get_html(html.json())


if __name__ == '__main__':
    main()