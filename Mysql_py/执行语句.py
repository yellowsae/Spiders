import pymysql
db = pymysql.connect(host='localhost',user='root',password='test4work',port=3306)
cursor = db.cursor()

# sql = 'create database if not exists test character set gbk'
touch = 'create database if not exists test character set gbk'
show_databses = 'show databases'
show_tables = 'show tables from test'
user = 'use test'
touch_table = 'create table test.books (book_id INT, title TEXT , status INT)'
describe = 'describe books' # 也可以使用 desc books
cursor.execute(user)
cursor.execute(describe)
cursor.execute('desc books')
print(cursor.fetchall())