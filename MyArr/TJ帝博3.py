import requests
import os
import urllib.request
import parsel

data = []


def get_url(url):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            response.encoding = 'gb18030' #解决乱码
            return response.text
    except RecursionError:
        return None


def get_info(html):
    selector = parsel.Selector(html)
    lis = selector.xpath(
        '//div[@class="clearfix shadow-box mod-info-flow"]//div[@class="mob-ctt"]/h3/a/@href'
    ).getall()
    for li in lis:
        info_url = 'http://bbs.zzbaorui.com/' + str(li)
        data.append(info_url)


def Index():
    for index in data:
        html_data = get_url(index)
        sele = parsel.Selector(html_data)
        infos = sele.xpath(
            '//div[@class="article-content-wrap"]/p/img/@src').getall()
        titles = sele.xpath(
            '//div[@class="pull-left wrap-left"]//h1[@class="t-h1"]/text()'
        ).get().split()
        for i, info in enumerate(infos):     # 这里使用 i + 1 就可以免去 命名为0张图片的问题 
            res = urllib.request.urlopen(info)
            try:
                with open(
                        './Img/' + titles[2] + titles[3] + str(i + 1 ) +
                        os.path.splitext(info)[-1], 'wb') as f:
                    f.write(res.read())
                    print('下载成功', info, titles[2] + titles[3] + str(i + 1 ))
            except:
                pass


if __name__ == "__main__":
    for page in range(1, 2):
        url = f'http://bbs.zzbaorui.com/list.asp?p={page}&classid=9'
        html = get_url(url)
        get_info(html)
        Index()
