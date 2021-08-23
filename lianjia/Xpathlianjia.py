# 使用xpath 爬取 链家房子数据
import requests
import parsel

url = 'https://cs.lianjia.com/ershoufang/pg1/'
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}
res = requests.get(url=url, headers=headers)
html_date = res.text
selector = parsel.Selector(html_date)
lis = selector.xpath('//ul[@class="sellListContent"]/li')

for li in lis:
    title = li.xpath('.//div[@class="title"]/a/text()').get()
    plase = li.xpath('.//div[@class="positionInfo"]/a/text()').getall()
    plase = "- ".join(plase)
    value = li.xpath('.//div[@class="totalPrice"]/span/text()').get() + "W"
    unitPrice = li.xpath('.//div[@class="unitPrice"]/span/text()').get()
    houseInfo = li.xpath('.//div[@class="houseInfo"]/text()').get()
    print(title, plase, value, unitPrice, houseInfo, sep=" | ")
