from fake_useragent import UserAgent
import requests 
import os 
from parsel import Selector
from time import sleep

if not os.path.exists('./e-hentai/Img/'):
    os.mkdir('./e-hentai/Img/')


# 发送请求
def get_url(url):
    heasers = {
        "User-Agent":UserAgent().chrome
    }
    proxy = '127.0.0.1:10809'
    proxies = {
        'http':'http://' + proxy,
        'https':'https://' + proxy
    }
    response = requests.get(url,headers=heasers,proxies=proxies)
    if response.status_code == 200:
        return response
    else:
        return None

# 获取所有图片 
def get_html(html):
    selector = Selector(html)
    img_all_url = selector.xpath('//div[@id="gdt"]/div//a/@href').getall()  # list 
    return img_all_url


# 下载保存 
def get_info(info,title):
    selector = Selector(info)
    img_url = selector.xpath('//div[@id="i3"]//img/@src').get()
    img_name = img_url.split('/')[-1]
    content = get_url(img_url)
    with open ('./e-hentai/Img/' + title + img_name , 'wb' ) as f :
        f.write(content.content)
        print('下载成功',title + img_name)
    

# 主函数 ，对每一个本子详情页进行访问 
def main(base_url,title):
    for url in base_url:
        # url = 'https://e-hentai.org/g/1869046/638fba71b5/'
        html = get_url(url)
        all_url = get_html(html.text)
        for img_url in all_url:
            info = get_url(img_url)
            get_info(info.text,title)

# 爬取主页的所有本子url 
def get_url_info(html):
    selector = Selector(html)
    base_url = selector.xpath('//table[@class="itg gltc"]//td[3]//a/@href').getall()
    benzi_name = selector.xpath('//div[@class="glink"]//text()').getall()
    
    # 返回所有本子的url和 name 
    return base_url , benzi_name

# 循环访问每一页的url
def start_url(url):
    html = get_url(url)
    info_url,title = get_url_info(html.text)
    return info_url,title

if __name__ == '__main__':
    # 爬取10页 
    for page in range(0,11): 
        url = f'https://e-hentai.org/tag/language:chinese/{page}'
        base_url , title = start_url(url)
        main(base_url,title)