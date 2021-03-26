from fake_useragent import UserAgent
from parsel import Selector
import requests

url = 'https://xchina.co/photos/model-%E6%9D%A8%E6%99%A8%E6%99%A8sugar.html'
headers = {
    'User-Agent':UserAgent().random
}
proxy = '127.0.0.1:10809'
proxies = {
    'http':'http://' + proxy,
    'https':'https://' + proxy
}
response  = requests.get(url,headers=headers,proxies=proxies)
selector = Selector(response.text)
all_urls = selector.xpath('//div[@class="item"]/a[1]/@href').getall()
print(all_urls)

# xpath 提取图片 ：  //div[@class="photos"]/a/div/@src  item
# 因为下一页的url 不好爬 ， 就不爬了 
