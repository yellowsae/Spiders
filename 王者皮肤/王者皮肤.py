# 导入模块
import requests
import pprint
import time

# 设置时间
start_time = time.time()

#  爬虫的一般思路
#1. 分析目标网页，确定爬取的url路径 ， headers参数  （难点）
bash_url = 'https://pvp.qq.com/web201605/js/herolist.json'
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}

# 2. 发送请求 -- requests模块。 模拟浏览器发送请求， 获取相应的数据
response = requests.get(url=bash_url, headers=headers)

# print(response.request.headers)

date_list = response.json()
pprint.pprint(date_list)

# 3 数据解析
for date in date_list:
    cname = date['cname'] # 英雄的名称
    ename = date['ename'] # 英雄的id
    try:
        skin_name = date['skin_name'].split('|') # 英雄的皮肤
    except Exception as e:
        print(e)
    # print(cname,ename,skin_name)
    for skin in range(1, len(skin_name) + 1):
        # 构建皮肤的循环
        img_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(
            ename) + '/' + str(ename) + '-bigskin-' + str(skin) + '.jpg'
        # print(img_url)
        # http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/515/515-bigskin-3.jpg
        # 请求图片数据
        # 下载
        img_date = requests.get(url=img_url, headers=headers).content

        # 4 保存数据 -- 保存在目标文件夹中
        with open('./img/' + cname + '-' + skin_name[skin - 1] + '.jpg',
                  mode='wb') as f:
            print('正在下载皮肤：', cname + '-' + skin_name[skin - 1])
            f.write(img_date)

print('程序花费的时间:', time.time() - start_time)
