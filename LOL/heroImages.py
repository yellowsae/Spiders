from fake_useragent import UserAgent 
import requests 
from time import sleep
from jsonpath import jsonpath  # 记住 jsonpath 的导入 
import json 
import os 


if not os.path.exists('./英雄联盟/img/'):
    os.mkdir('./英雄联盟/img/')


def get_url(url):
    headers = {
        'User-Agent':UserAgent().random
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        # response.encode('utf-8')  #  这里的json 数据不能用 utf-8 编码 
        return response
    else:
        return None


# 获取 皮肤ID  和 皮肤name   
def get_html(html):
    skin_ID = jsonpath(html,'$..skinId')
    skin_Name = jsonpath(html,'$..name')
    hero_Name = jsonpath(html,'$..heroName')
    skin_img_Name = hero_Name + skin_Name
    return skin_ID, skin_Name, hero_Name[0]


# 开始url ， 获取hero_ID 
def start_url(url):
    response = requests.get(url)
    # response.encode('utf-8') 
    hero_ID = jsonpath(response.json(),'$..heroId')
    return hero_ID

# 保存img 
def get_content(img_content, skin_img_Name, hero_Name):
    if not os.path.exists('./英雄联盟/img/' + hero_Name + '/'):
        os.mkdir('./英雄联盟/img/' + hero_Name + '/')
    with open('./英雄联盟/img/' + hero_Name + '/' + skin_img_Name  + ".jpg", 'wb' ) as f: 
        f.write(img_content)
        print('保存成功-----' + skin_img_Name )
    

# 主函数 
def main(hero_ID):
    for heroID in hero_ID:
        html = get_url(f'https://game.gtimg.cn/images/lol/act/img/js/hero/{heroID}.js')
        skin_ID, skin_img_Name, hero_Name= get_html(html.json())
        # 去重 
        # del skin_img_Name[0] 
        skin_img_Name.pop(0)

        base_url = [] 
        for skinID in skin_ID:
            base_url.append(f'https://game.gtimg.cn/images/lol/act/img/skin/big{skinID}.jpg')
        try:
            for skin_Name , img_url in zip(skin_img_Name,base_url):
                img_content = get_url(img_url)
                get_content(img_content.content, skin_Name,hero_Name)
        except:
            pass


# 选择英雄ID 
if __name__ == '__main__':
    url = 'http://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
    hero_ID = start_url(url)
    main(hero_ID)