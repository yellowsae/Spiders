import requests # 网络请求模块
from bs4 import BeautifulSoup # 数据分析
from prettytable import PrettyTable # 列表打印

# 实例化表格
table = PrettyTable(['编号', '歌曲名称', '歌手', '歌曲时长'])

url = r"https://www.xiami.com/list?page=1&query=%7B%22genreType%22%3A1%2C%22genreId%22%3A%2220%22%7D&scene=genre&type=song"
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
}
response = requests.get(url=url, headers=headers)

# step01: 将文本内容实例化出bs对象
soup_obj = BeautifulSoup(response.text, "lxml")

# step02: 查找标签
main = soup_obj.find("div",
                     attrs={"class":
                            "table idle song-table list-song"}) #使用了attr()获取标签

# step03: 查找存放歌曲信息的tbody标签
tbody = main.select(".table-container>table>tbody")[0] # 使用了 select()获取的方法

# step04: tbody标签中的每个tr都是一首歌曲
tr = tbody.find_all("tr") # find_all() 方法

# step04: 每个tr里都存放有歌曲信息，所以直接循环即可
for music in tr:
    name = music.select(".song-name>a")[0].text # .text  # 获取文本
    singer = music.select(".COMPACT>a")[0].text
    time_len = music.select(".duration")[0].text
    table.add_row(
        [tr.index(music) + 1, name, singer,
         time_len]) # .add_row() 以表单方式进行数据存储, index(music)+1 表示列数加1， 包括了第一行的表示头

# step05: 打印信息
print(table)

# 结果如下
"""
+------+--------------------------------------------------+--------------------+----------+
| 编号 |                     歌曲名称                     |        歌手        | 歌曲时长 |
+------+--------------------------------------------------+--------------------+----------+
|  1   | Love Story (Live from BBC 1's Radio Live Lounge) |    Taylor Swift    |  04:25   |
|  2   |                Five Hundred Miles                |        Jove        |  03:27   |
|  3   |    I'm Gonna Getcha Good! (Red Album Version)    |    Shania Twain    |  04:30   |
|  4   |                     Your Man                     |    Josh Turner     |  03:45   |
|  5   |             Am I That Easy To Forget             |     Jim Reeves     |  02:22   |
|  6   |                   Set for Life                   |    Trent Dabbs     |  04:23   |
|  7   |                    Blue Jeans                    |  Justin Rutledge   |  04:25   |
|  8   |                    Blind Tom                     | Grant-Lee Phillips |  02:59   |
|  9   |                      Dreams                      |   Slaid Cleaves    |  04:14   |
|  10  |                  Remember When                   |    Alan Jackson    |  04:31   |
|  11  |                Crying in the Rain                |    Don Williams    |  03:04   |
|  12  |                    Only Worse                    |    Randy Travis    |  02:53   |
|  13  |                     Vincent                      | The Sunny Cowgirls |  04:22   |
|  14  |           When Your Lips Are so Close            |    Gord Bamford    |  03:02   |
|  15  |                  Let It Be You                   |    Ricky Skaggs    |  02:42   |
|  16  |                  Steal a Heart                   |    Tenille Arts    |  03:09   |
|  17  |                      Rylynn                      |     Andy McKee     |  05:13   |
|  18  |        Rockin' Around The Christmas Tree         |     Brenda Lee     |  02:06   |
|  19  |            Love You Like a Love Song             |    Megan & Liz     |  03:17   |
|  20  |               Tonight I Wanna Cry                |    Keith Urban     |  04:18   |
|  21  |           If a Song Could Be President           |   Over the Rhine   |  03:09   |
|  22  |                   Shut'er Down                   |   Doug Supernaw    |  04:12   |
|  23  |                     Falling                      |  Jamestown Story   |  03:08   |
|  24  |                     Jim Cain                     |   Bill Callahan    |  04:40   |
|  25  |                  Parallel Line                   |    Keith Urban     |  04:14   |
|  26  |                 Jingle Bell Rock                 |    Bobby Helms     |  04:06   |
|  27  |                    Unsettled                     |  Justin Rutledge   |  04:01   |
|  28  |                Bummin' Cigarettes                |    Maren Morris    |  03:07   |
|  29  |              Cheatin' on Her Heart               |    Jeff Carson     |  03:18   |
|  30  |             If My Heart Had a Heart              |   Cassadee Pope    |  03:21   |
+------+--------------------------------------------------+--------------------+----------+

"""
