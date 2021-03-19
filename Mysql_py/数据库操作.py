import  pymysql

def main():
    no = int(input("编号: "))
    name = input('名字: ')
    loc = input('所在地 : ')

    # 创建连接对象
    con = pymysql.connect(host='localhost',port=3306,database='hrs',charset='utf8',user='root',password='test4work')
    try:
        # 通过连接对象获取游标
        with con.cursor() as cursor:
            # 通过游标执行 SQL 语句 并获得结果
            result = cursor.execute(
                'insert into tb_dept values (%s , %s , %s )',
                (no, name , loc )  # 对数据新操作, 上边输入的一样
            )
            if result == 1 :
                print('添加成功 !')
            # 操作成功提交事务
            con.commit()
    finally:
        # 关闭连接释放资源
        con.close()

if __name__ == '__main__':
    main()
