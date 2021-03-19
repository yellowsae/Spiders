# 问题
# 你想创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序。

"""
解决方案
为了能控制一个字典中元素的顺序，你可以使用 collections 模块中的 OrderedDict 类。 在迭代操作的时候它会保持元素被插入时的顺序，示例如下：
"""
from collections import OrderedDict

d = OrderedDict()

d['foo'] = 'test'
d['bar'] = 1
d['test'] = 123
print(type(d))  # <class 'collections.OrderedDict'> 
for Key in d:
    print(Key,d[Key])

import json
json.dumps(d)
print(d)