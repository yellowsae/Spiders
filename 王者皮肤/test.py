import requests

url = "https://pvp.qq.com/web201605/herolist.shtml"
print(requests.get(url=url).status_code)
