# 问题
# 怎样在数据字典中执行一些计算操作（比如求最小值、最大值、排序等等）？

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

"""
解决办法
为了对字典值执行计算操作，通常需要使用 zip() 函数先将键和值反转过来。 比如，下面是查找最小和最大股票价格和股票值的代码：
"""

max_dict = max(zip(prices.values(),prices.keys()))  # zip()  将字典进行 key 和 value 反转 , 再使用max() min() 函数求出最小值最大值
min_dict = min(zip(prices.values(),prices.keys()))  # 
# sum_dict = sum(zip(prices.values(),prices.keys()))  # 求和不行 
print(max_dict,min_dict)

# 执行这些计算的时候，需要注意的是 zip() 函数创建的是一个只能访问一次的迭代器。 
dict_prices = zip(prices.values(),prices.keys())
print(max(dict_prices))
# print(min(dict_prices))   # Error 


prices_sortde = sorted(zip(prices.values(),prices.keys()))  # 使用 sortde() 进行排序， 也要使用zip() 进行 key 和 value 的反转
print(prices_sortde)

# 如果你在一个字典上执行普通的数学运算，你会发现它们仅仅作用于键，而不是值。比如： 
# 计算时的 dict 需要的时 key 而不是 value 
print(min(prices))
print(min(prices.values()))
print(max(prices.values()))
print(sum(prices.values()))  # sum 求和

# 存储为 list 
a = []
a.append(prices.values())
print(a)