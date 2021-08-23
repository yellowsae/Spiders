"""
问题
怎样从一个集合中获得最大或者最小的 N 个元素列表？
"""

#heapq 模块有两个函数：nlargest() 和 nsmallest() 可以完美解决这个问题。

import heapq

list_test = [123,5123,512,1,51,20.123]
print(max(list_test))  # 直接获取最大的数
print(min(list_test))  # 直接获取最小的数

# 如果 获取 最大的 N 个数 
print(heapq.nlargest(4,list_test))  # 获取最大的3个元素
print(heapq.nsmallest(3,list_test)) # 获取最小的3个元素

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])  # 获取最小的3个数据
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price']) # 获取最大的3个数据
# 译者注：上面代码在对每个元素进行对比的时候，会以 price 的值进行比较。

print(cheap)
print(expensive)
