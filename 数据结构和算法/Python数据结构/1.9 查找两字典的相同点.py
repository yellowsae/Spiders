
# 怎样在两个字典中寻寻找相同点（比如相同的键、相同的值等等）？

a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

print( a.keys() & b.keys() )  # keys 的相同的key
print( a.keys() - b.keys() )  # 不同的key

# 不用keys() 也可以使用 items() ,使用 items 返回的是 执行操作的集合
print( a.items() & b.items())

# 这些操作也可以用于修改或者过滤字典元素。 比如，假如你想以现有字典构造一个排除几个指定键的新字典。 下面利用字典推导来实现这样的需求：
c = {key:a[key] for key in a.keys() - {'z', 'w'}} 
print(c)