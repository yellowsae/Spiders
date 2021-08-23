
"""
问题
怎样实现一个键对应多个值的字典（也叫 multidict）？
"""

"""
解决方案
一个字典就是一个键对应一个单值的映射。如果你想要一个键映射多个值，
那么你就需要将这多个值放到另外的容器中， 比如列表或者集合里面。比如，你可以像下面这样构造这样的字典：

一个 key 映射多个value值 , 不就是values定义为一个list tuple , 里边放多个值
"""

dict_test = {
    'a':[1,2,3,4],
    'b':('test',1,2,4),
    'c':{1,2,3}  # set
}
print(type(dict_test['c']))
print(dict_test)

#你可以很方便的使用 collections 模块中的 defaultdict 来构造这样的字典。 defaultdict 的一个特征是它会自动初始化每个 key 
# 刚开始对应的值，所以你只需要关注添加元素操作了。比如：
# 使用 collections.defaultdic 构造出的字典，会初始化key ,可以使用 append() 添加值, 但是添加值的类型为 list 类型
# 合理方法
from collections import defaultdict
d = defaultdict(list)  # value 只能是 list 类型 ,因为tuple 和 set 不可变 
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(type(d['b']))


# 简单的方法 
# 一般来讲，创建一个多值映射字典是很简单的。但是，如果你选择自己实现的话，
# 那么对于值的初始化可能会有点麻烦， 你可能会像下面这样来实现

pairs = [1,2,3]
d = {}
for key,value in pairs: # 需要循环的list 
    if key not in d:
        d[key] = [] # 初始化为一个list 
    d[key].append(1)

# 或者使用 defaultdist
d = defaultdict(list)
for key,value in pairs:
    d[key].append(value)