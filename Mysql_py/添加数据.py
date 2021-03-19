import pymysql
# from pymysql.cursors import DictCursor


def main():
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         password='test4work')
    try:
        with db.cursor() as cursor:
            cursor.execute('show databases')
            cursor.execute('drop database if exists xky ')
            cursor.execute('create database xky default charset utf8')
            cursor.execute('use xky')
            # 创建表
            tb_college = """create table tb_college
                        (
                        collid 		int auto_increment comment '编号',
                        collname 	varchar(50) not null comment '名称',
                        collintro 	varchar(500) default '' comment '介绍',
                        primary key (collid)
                        )
                        """
            tb_student = """create table tb_student 
                        (
                            stuid		int not null comment '学号' ,
                            stuname		varchar(20) not null comment '姓名' ,
                            stusex		boolean default 1 comment '性别',
                            stubirth	dete not null comment '出生日期',
                            stuaddr		varchar(255) default ' ' comment '籍贯',
                            collid		int not null commit '所属学院',
                            primary key(studi),
                            foreign key(collid) references tb_college (collid) 
                        )
            """

            tb_teacher = """
            create table tb_teacher
                        (
                        teaid 		int not null comment '工号',
                        teaname 	varchar(20) not null comment '姓名',
                        teatitle 	varchar(10) default '助教' comment '职称',
                        collid 		int not null comment '所属学院',
                        primary key (teaid),
                        foreign key (collid) references tb_college (collid)
                        )
            """

            tb_course = """
            create table tb_course
                        (
                        couid 		int not null comment '编号',
                        couname 	varchar(50) not null comment '名称',
                        coucredit 	int not null comment '学分',
                        teaid 		int not null comment '授课老师',
                        primary key (couid),
                        foreign key (teaid) references tb_teacher (teaid)
                        )"""

            tb_record = """
            create table tb_record
                (
                recid 		int auto_increment comment '选课记录编号',
                sid 		int not null comment '选课学生',
                cid 		int not null comment '所选课程',
                seldate 	datetime default now() comment '选课时间日期',
                score 		decimal(4,1) comment '考试成绩',
                primary key (recid),
                foreign key (sid) references tb_student (stuid),
                foreign key (cid) references tb_course (couid),
                unique (sid, cid)
                )
            """
            # 创建5个表
            cursor.execute(tb_college)
            cursor.execute(tb_student)
            cursor.execute(tb_teacher)
            cursor.execute(tb_course)
            cursor.execute(tb_record)
            cursor.execute('show tables')
            # cursor.execute('drop database if exists school ')
            # cursor.execute('create database school default charset utf8')
            # cursor.execute('use school')
            result = cursor.fetchall()
            print(result)
    finally:
        db.close()


if __name__ == '__main__':
    main()
