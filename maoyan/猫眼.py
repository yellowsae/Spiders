# 请求链接：https://maoyan.com/board/4
# 爬取目标：猫眼 TOP100 的电影名称、排名、主演、上映时间、评分、封面图地址，数据保存为 CSV 文件
# 涉及知识：请求库 requests、解析库 lxml、Xpath 语法、CSV 文件储存

import requests
from lxml import etree 
import csv
import os
#头部伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}
#爬取当前页面
def index_page(number):
    url = 'https://maoyan.com/board/4?offset=%s' % number
    response = requests.get(url=url,headers=headers)
    return response.text
#爬取页面信息
def parse_page(content):
    tree = etree.HTML(content)
    # rank
    ranking = tree.xpath("//dd/i/text()")
    # name
    movie_name = tree.xpath('//p[@class="name"]/a/text()')
    # actor
    performer = tree.xpath("//p[@class='star']/text()")
    performer = [p.strip() for p in performer]
    # 上映时间
    releasetime = tree.xpath('//p[@class="releasetime"]/text()')
    # scores
    score1 = tree.xpath('//p[@class="score"]/i[@class="integer"]/text()')
    score2 = tree.xpath('//p[@class="score"]/i[@class="fraction"]/text()')
    score = [score1[i] + score2[i] for i in range(min(len(score1), len(score2)))]
    # pic
    movie_img = tree.xpath('//img[@class="board-img"]/@data-src')
    #返回信息
    return zip(ranking, movie_name, performer, releasetime, score, movie_img)
#安行保存结果
def save_result(result):
    if not os.path.exists('./maoyan.csv'):
        os.mkdir('./maoyan.csv')
    with open('maoyan.csv','a') as f:
        writer = csv.writer(f)
        writer.writerow(result)
if __name__ == "__main__":
    print("开始爬取")
    #共10页
    for i in range(0,100,10):
        index = index_page(i)
        results = parse_page(index)
        for item in results:
            save_result(item)
    print("end")