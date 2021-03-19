from fake_useragent import UserAgent
import requests 
import parsel
import os 
from time import sleep

if not os.path.exists('./合集/xiuren/'):
    os.mkdir('./合集/xiuren/')


def get_url(url):
    headers = {
        'User-Agent':UserAgent().chrome
    }
    proxy = '127.0.0.1:10809'
    proxies = {
        'http':'http://' + proxy,
        'https':'https://' + proxy
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        response.encoding='utf-8'
        return response.text
    else:
        return None

def get_html(html):
    selector = parsel.Selector(html)
    base_url = []
    next_url = selector.xpath('//div[@class="pagination1"][1]//ul/a/@href').getall()
    for url in next_url:
        base_url.append('https://www.jpmnb.cc/' + url)
    base_url.pop() # 删除最后一个url 
    return base_url

def get_img_html(img_html):
    selector = parsel.Selector(img_html)
    # img_urls 
    urls = selector.xpath('//p/img/@src').getall()
    title = selector.xpath('//p/img[1]/@alt').get()
    img_url = []
    # 进行拼接然后返回 
    for url in urls:
        img_url.append('https://p.jpmnb.cc' + url) 
    # 返回下载
    return img_url , title


def save_content(img_url,title):
    for url in img_url:
        try : 
            # 图片后缀 命名 
            img_name = url.split('/')[-1]
            res = requests.get(url)
            with open('./合集/xiuren/' + title + '_'+ img_name , 'wb' ) as f :
                f.write(res.content)
                print('下载成功',title + img_name)
        except:
            print('Error')

def main(base_url):
    # 合集 ,再传入下一篇的合集就行
    for url in  base_url:
        # url = 'https://www.jpmnb.cc/Xrqj/XiaoYu/13380.html'
        # 停2s 爬取一份套图
        print('正在爬取' + url + '的套图')
        # sleep(2)
        html = get_url(url)
        # 下一页url
        base_url = get_html(html) 
        # print(base_url)
        try: 
            for info_url in base_url:
                # 3s 
                # sleep(3)
                img_html = get_url(info_url) 
                # 获取到每一页 img 的url 和 title
                img_url, title = get_img_html(img_html)
                save_content(img_url,title)
        except:
            print('访问出错')

# 多次爬取
def get_urls():
    # 爬取10页套图 
    base_url = []
    try : 
        for page in range(1,3):
            print('正在爬取第' + str(page) + '页')
            url = f'https://www.jpmnb.cc/plus/search/index.asp?keyword=%E6%9D%A8%E6%99%A8%E6%99%A8&searchtype=title&p={page}'
            # 停止0.5s 访问下一页
            sleep(0.5) 
            html = get_url(url)
            selector = parsel.Selector(html)
            urls =  selector.xpath('//div[@class="title"]/h2/a/@href').getall()
            for info in urls:
                base_url.append('https://www.jpmnb.cc' + info)
    except:
        print('第' + str(page) + '页出错')
    return base_url

if __name__ == '__main__':
    base_url = get_urls()
    main(base_url)
    print('下载完成')


#  最终版
"""
问题 

没有多线程 

命名问题 ： 不是以套图名称进行命名 ， 而是以url后缀的编码命名 
在命名使用  open( "./" + title + str (i + 1 ))   , i 在循环时使用 enumerate() ,定义就行


路径问题 
没有进行分类， 制动创建按照套图的名称进行命名  ， （可以进行解决 ）
思路 ： 再传递 图片url，和 title套图名称时 ， os.mkdir("./xiuren/" + title   ) , 


"""
