import pymongo

#  链接数据库
client = pymongo.MongoClient('mongodb://127.0.0.1:27017')

# 获取某数据库的游标
db = client.school
for student in db.students.find():
	print('学号:' , student['stuid'])
	print('姓名: ', student['name'])
	# print('电话 :', student[])
	# print('性别 :', student['gender'])

