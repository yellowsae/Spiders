import requests
import parsel

url = 'https://maoyan.com/board/4?offset=0'
try:
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
except:
    pass
print(response.status_code)
# print(response.text)
# html_date = response.text
# print(html_date)
# get_info = BeautifulSoup(html_date, 'lxml')
# div_info = get_info.find('div', class_='board-wrapper')
# print(div_info)
selector = parsel.Selector(response.text)
lis = selector.xpath('//dl[@class="board-wrapper"]/dd').get()
print(lis)
# for li in lis:
#     li_name = li.xpath('.//p[@class="name"]//text()').get()
#     li_star = li.xpath('.//p[@class="star"]//text()').get().split() # 去掉空格
#     li_time = li.xpath('.//p[@class="releasetime"]//text()').get()
#     li_score = li.xpath('.//p[@class="score"]/i[1]/text()').get() + li.xpath(
#         './/p[@class="score"]/i[2]/text()').get()
#     print(li_name, li_star, li_time, li_score, sep=" | ")
