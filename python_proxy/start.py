# 使用 SOCKS5配置代理
# 需要进行安装 pip install Pysocks
import socket
import socks
from urllib import request
from urllib.error import URLError

# 正常使用代理
socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 1080)
socket.socket = socks.socksocket
try:
    response = request.urlopen('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
"""
{
  "args": {},
  "headers": {
    "Accept-Encoding": "identity",
    "Host": "httpbin.org",
    "User-Agent": "Python-urllib/3.9",
    "X-Amzn-Trace-Id": "Root=1-60101e72-1b3cf8bf4f60b95b337a414f"
  },
  "origin": "8.210.158.72",  # 香港 阿里云
  "url": "http://httpbin.org/get"
}

"""
