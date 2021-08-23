#!/usr/bin/python3
# -*- conding:utf-8 -*-
"""

 爬虫 ：  所谓爬虫就是 模拟客户端去请求服务端的数据
        一般步骤 ：
                1  确定目标的地址(url)
                2  代码请求地址数据（伪装）
                3  数据解析
                4  数据保存

目的 ： 爬取链家房子的数据信息
        房子标题
        总价
        单价
        地址
        信息

parsel
requests
csv

"""

import requests
import parsel
import csv

url = 'https://cs.lianjia.com/ershoufang/pg1/'
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}
res = requests.get(url=url, headers=headers)
html_date = res.text # html_date --> str

# 转化数据类型
selcetor = parsel.Selector(html_date) # selcetor --> class  对象
# 解析数据 ： 正则  xpath  css 选择器
print(type(selcetor))
# css 选择器
lis = selcetor.css('.clear.LOGCLICKDATA') # 空格使用 . 表示 ,  取出所有的li标签

for li in lis:
    # 二次提取
    title = li.css('.title a::text ').get()
    plase = li.css(
        '.positionInfo a::text').getall() # getall() 获取所有标签,返回是一个list,
    # 列表合并 join()
    plase = "- ".join(plase)
    #
    value = "总价" + li.css('.totalPrice span::text').get() + "万"
    unitPrice = li.css('.unitPrice span::text').get()
    houseInfo = li.css('.houseInfo::text').get()
    print(title, plase, value, unitPrice, houseInfo, sep="  |  ")
    with open('lianjia.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([title, plase, value, unitPrice, houseInfo])

# with open('lianjia.csv', mode='a', encoding="UTF-8", newline=" ") as f:
#     write_info = csv.writer(f)
#     write_info.writerow(row)

# lis = selcetor.xpath('//ul[@class="sellListContent"]/li')
# for li in lis:
#     title = li.xpath(
#         './/div[@class="info clear"]//div[@class="title"]/a/text()').get()
#     print(title)
"""
requests 请求回到的对象可以使用 xpath 提取数据 ，也可以使用 css选择器
css 选择器 语法 ：

对象.css(".一个class = 的标签") 如果标签中有空格要使用.表示 , 最前的.表示匹配从当前开始

li.css('.title a::text').get()
.title     是css 匹配到的标签
a      title 下的标签
::text     获取a标签的文本内容
.get()     requests包中 对象获取请求的包
.getall()     请求获取所有标签 获取到是一个列表类型
" - ".join()       将列表使用- 进行合并

"""

# 总结 ： 一般爬取静态网页的内容 可以使用xpath  css 选择器 都行但是Linux 使用的csv 保存文件还是有点问题
