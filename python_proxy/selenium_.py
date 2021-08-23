from selenium import webdriver

proxy = '127.0.0.1:10808'
# Chrome , 不同浏览器的配置代理不同
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=http://' + proxy)  # HTTP
chrome_options.add_argument('--proxy-server=socks5://' + proxy) # SOCKS5
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('http://httpbin.org/get')
"""
{
  "args": {}, 
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
    "Accept-Encoding": "gzip, deflate", 
    "Accept-Language": "zh-CN,zh;q=0.9", 
    "Host": "httpbin.org", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-601037ba-24a68db229a8ddf02a013126"
  }, 
  "origin": "8.210.158.72", 
  "url": "http://httpbin.org/get"
}
"""
