import pymysql 
db = pymysql.connect(host='localhost',user='root',password='test4work',port=3306)
cursor = db.cursor()
cursor.execute('select version()')
date = cursor.fetchone()
print('Database version :',date)
# Database version : ('5.7.20-log',) 
# 创建一个数控库
cursor.execute('create database spiders default character set utf8')  # 数据库语句， 很容易出错 
db.close() 