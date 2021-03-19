# 检测 IP 质量
import requests
import parsel
import time


def check_ip(proxy_ip):
    #需要一个请求头
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    for ip in proxy_ip:
        try:
            respones = requests.get(url='https://www.baidu.com/',
                                    headers=headers,
                                    proxies=ip,
                                    timeout=1)
            # proxies 使用的代理IP, timeout = 1 表示请求时间超出1秒会报错 , 达到筛选的目的
            can_user = [] # 定义一个可用代理的list
            if respones.status_code == 200: # respones.status_code 表示相应请求的状态码
                can_user.append(ip)
        except:
            print('当前ip质量不行', ip)
        # 不报错执行 else
        else:
            print("当前IP质量可以使用", ip)
    return can_user


proxy_list = []


def get_url(url):
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    respond = requests.get(url, headers=headers)
    html_date = respond.text
    selector = parsel.Selector(html_date)
    trs = selector.xpath(
        '//table[@class="table table-bordered table-striped"]//tbody/tr'
    ) # 这里要精确到每一个数据的最外层才能取出所有的数据
    for tr in trs:
        tr_ip = tr.xpath('./td[1]/text()').get()
        tr_port = tr.xpath('./td[2]/text()').get()
        # print(tr_ip,tr_port)
        ip_port = tr_ip + ':' + tr_port
        # 使用字典进行数据接收
        port_dict = {
            "http": "http://" + ip_port,
            "https": "https://" + ip_port,
        }
        # 列表保存
        proxy_list.append(port_dict)
        print("保存成功", proxy_list)


for page in range(1, 11):
    url = f'https://www.kuaidaili.com/free/inha/{page}'
    print(f'===============正在爬取第{page}页==================')
    time.sleep(1) # 休眠1秒
    get_url(url)
print("获取到的代理IP有：", len(proxy_list), "个")

print('============正在检测IP质量==============')
user = check_ip(proxy_list)
print('质量高的代理: ', user)
print('质量高的代理有', len(user), '个')

