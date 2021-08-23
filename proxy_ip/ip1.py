
# 爬取免费代理
import requests 
import parsel
import time

"""
parsel是 Scrapy爬虫框架  用作数据解析的 

"""
"""
代理形式 
{
    'http':'http://ip+端口'
    'https':'https://ip+端口'
}
"""

#定义一个容器进行数据的保存 
proxy_list = []
def get_url(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    respond = requests.get(url,headers=headers)
    html_date = respond.text
    selector = parsel.Selector(html_date)
    trs = selector.xpath('//table[@class="table table-bordered table-striped"]//tbody/tr')  # 这里要精确到每一个数据的最外层才能取出所有的数据 
    for tr in trs:
        tr_ip = tr.xpath('./td[1]/text()').get()  #  
        tr_port = tr.xpath('./td[2]/text()').get()
        # print(tr_ip,tr_port)
        ip_port = tr_ip +':'+tr_port
        # 使用字典进行数据接收 
        port_dict = {
            "http":"http://"+ip_port,
            "https":"https://"+ ip_port,
        }
        # 列表保存
        proxy_list.append(port_dict)
        print("保存成功",proxy_list)

url = 'https://www.kuaidaili.com/free/'
get_url(url)

print(proxy_list)
print("获取到的代理IP有：",len(proxy_list),"个")