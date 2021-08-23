import requests
import socket
# import socks
# 需要 安装 pip install 'requests[socks]'
proxy = '127.0.0.1:10808'
proxies = {'http': 'socks5://' + proxy, 'https': 'socks5://' + proxy}
# 使用 socks5 代理 和 https 代理不一样
# proxies = {'http': 'http://' + proxy, 'https': 'https://' + proxy}
try:
    response = requests.get('http://httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('ERROR', e.args)

# 另一种配置的方法
# 需要导入 import sockers socks

# socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 10808)
# socket.socket = socks.socksocket
# try:
#     response = requests.get('http://httpbin.org/get')
#     print(response.text)
# except requests.exceptions.ConnectionError as e:
#     print('ERROR', e.args)

# 建议使用第一种
