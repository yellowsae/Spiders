from jsonpath import jsonpath
from fake_useragent import UserAgent
import requests
from urllib.request import urlopen
import os

if not os.path.exists('./皮肤图片'):
    os.mkdir('./皮肤图片')

def get_info(hero_json):
    # 英雄id
    ename = jsonpath(hero_json,'$..ename')
    # 英雄名称
    cname = jsonpath(hero_json,'$..cname')
    # 皮肤名称
    skin_name = jsonpath(hero_json,'$..skin_name')
    skin_pifu = []
    for skin in skin_name:
        pifu = skin.split('|') # 皮肤类型分割
        skin_pifu.append(pifu)

    for name ,id, skin in zip(cname,ename,skin_pifu):
        for i in range(1,len(skin)):
            # img_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/522/522-bigskin-3.jpg'
            # 皮肤的url
            base_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(id) + '/' + str(id) +'-bigskin-'+ str(i) +'.jpg'
            img_content = requests.get(base_url).content
            # img = urlopen(base_url)
            with open('./皮肤图片/'+ name + '--' + skin[i-1] + '.jpg', mode='wb') as f :
                f.write(img_content)
                print('正在下载----',skin[i])
            pass
    # print(ename)
    # print(cname)
    # print(skin_name)
def get_url(url):
    headers = {
        "User-Agent":UserAgent().random
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.json()
if __name__ == '__main__':
    url = 'https://pvp.qq.com/web201605/js/herolist.json'
    hero_json = get_url(url)
    get_info(hero_json)

"""
总结 ： 
    1， 学到了使用jsonpath 处理数据
    2,  学到了json数据中[]进行分割， split('|'), 返回的是list类型
    3,  学到了url 的拼接 
"""