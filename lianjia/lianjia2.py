# 多个页面获取
import requests
import parsel
import csv
for pape in range(1, 10, 1): # 可爬取100页
    url = f'https://cs.lianjia.com/ershoufang/pg{pape}'
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    res = requests.get(url=url, headers=headers)
    html_date = res.text # html_date --> str
    # 转化数据类型
    selcetor = parsel.Selector(html_date) # selcetor --> class  对象
    # 解析数据 ： 正则  xpath  css 选择器
    # css 选择器
    lis = selcetor.css('.clear.LOGCLICKDATA') # 空格使用 . 表示 ,  取出所有的li标签
    for li in lis:
        # 二次提取
        title = li.css('.title a::text ').get()
        plase = li.css(
            '.positionInfo a::text').getall() #getall() 获取所有标签,返回是一个list
        # 列表合并 join()
        plase = "- ".join(plase)
        value = "总价" + li.css('.totalPrice span::text').get() + "万"
        unitPrice = li.css('.unitPrice span::text').get()
        houseInfo = li.css('.houseInfo::text').get()
        row = [title, plase, value, unitPrice, houseInfo]
        print(title, plase, value, unitPrice, houseInfo, sep="  |   ")
    with open('lianjia.csv', mode='a', encoding="UTF-8", newline=" ") as f:
        write_info = csv.writer(f)
        write_info.writerow(row)

    # lis = selcetor.xpath('//ul[@class="sellListContent"]/li')
    # for li in lis:
    #     title = li.xpath(
    #         './/div[@class="info clear"]//div[@class="title"]/a/text()').get()
    #     print(title)
