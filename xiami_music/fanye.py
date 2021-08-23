import requests # 网络请求模块
from prettytable import PrettyTable # 列表打印
import time
import parsel
# 实例化表格
table = PrettyTable(['编号', '歌曲名称', '歌手', '歌曲时长'])


def get_url(url):
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    }
    response = requests.get(url, headers=headers)
    html_date = response.text
    selector = parsel.Selector(html_date)
    lis = selector.xpath('//div[@class="table-container"]//tr')
    for li in lis:
        name = li.xpath('.//div[@class="song-name em"]/a/text()').get()
        songer = li.xpath('.//div[@class="singers COMPACT"]//text()').get()
        song_time = li.xpath(
            './/div[@class="duration-container ops-container"]//text()').get()
        print(name, songer, song_time, sep=" | ")
        table.add_row([lis.index(li), name, songer, song_time])


for pape in range(1, 11):
    url = f"https://www.xiami.com/list?page={pape}&query=%7B%22genreType%22%3A1%2C%22genreId%22%3A%2220%22%7D&scene=genre&type=song"
    time.sleep(0.2)
    print(f"=============第{pape}页==================")
    get_url(url)
    pass
print(table)
