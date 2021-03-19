import pymysql
db = pymysql.connect(host='localhost',user='root',password='test4work',port=3306)
cursor = db.cursor()
sql = 'create table if not exists students (id VARCHAR(255) not null, name VARCHAR(255) not null , age int not null , PRIMARY key(id))'
cursor.execute(sql)
db.close()
