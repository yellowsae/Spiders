from fake_useragent import UserAgent
import requests
import os 
from parsel import Selector
from time import sleep

if not os.path.exists('./toreent/'):
    os.mkdir('./toreent')


def get_url(url):
    headers = {
        "User-Agent":UserAgent().random
    }
    proxy = '127.0.0.1:10809'
    proxies = {
        'http':'http://' + proxy,
        'https':'https://' + proxy
    }
    sleep(1)    # 休眠1s 
    response = requests.get(url,headers=headers,proxies=proxies)
    if response.status_code == 200:
        return response
    else:
        return None

def get_html(html):
    selector = Selector(html)
    base_url = []
    img_all = selector.xpath('//div[@class="table-responsive"]//td[2]//a/@href').getall()
    for img in img_all:
        base_url.append('https://sukebei.nyaa.si' + img)
    return base_url

def parse_data(data):
    selector = Selector(data)
    title = selector.xpath('//h3[@class="panel-title"]/text()').get().split()
    title = ''.join(title)
    torrent = selector.xpath('//div[@class="panel-footer clearfix"]/a[1]/@href').get()
    torrent_url = 'https://sukebei.nyaa.si' + torrent
    return torrent_url,title

def save_date(content,title):
    torrent_content = get_url(content)
    with open('./toreent/' + title + '.torrent', 'wb') as f:
        f.write(torrent_content.content)
        print('save successful ')
    pass


def main():
    for page in range(1,11):
        url = f'https://sukebei.nyaa.si/?tdsourcetag=s_pctim_aiomsg&p={page}'
        html = get_url(url)
        base_url = get_html(html.text)
        for img_url in base_url:
            data = get_url(img_url)
            content,title = parse_data(data.text)
            save_date(content,title)

if __name__ == "__main__":
    main()

# prefection

