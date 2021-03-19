# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 记得要 打开 setting 里的 pipeline


class XiaoshuoPipeline(object):
    # 定义一个函数打开文件
    # def open_file(self, spider):
    def __init__(self):
        self.file = open('xiaoshuo.txt', 'w', encoding='utf-8')

    # 写内容
    def process_item(self, item, spider):
        title = item['title']
        content = item['content']
        # 内容拼接
        # info = str(title) + '\n' + str(content) + '\n'
        info = str(title) + '\n' + str(content) + '\n'
        # info = title + '\n'
        self.file.write(info)
        self.file.flush() # 刷新
        return item

    # 关闭文件
    def close_file(self, spider):
        self.file.close()


"""
出现这样的报错 ： 

AttributeError:'XiaoshuoPipeline' object has no attribute'file'   AttributeError：“ XiaoshuoPipeline”对象没有属性“ file” 

也就是没有找到 定义的file对象 

所以定义初始的变量时，使用 def __init__(self): 定义 


"""
