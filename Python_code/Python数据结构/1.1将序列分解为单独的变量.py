
# 参考教程 : https://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p01_unpack_sequence_into_separate_variables.html 

"""
1.1 将序列分解为单独的变量
问题
现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N 个变量？
"""
tuple_1 = (1,2,3,4,5)
# # 进行拆解 
# for num in tuple_1:
#     print(num)

# 赋值给N个变量 
a , b, c, d,e = tuple_1
print(a,b,c,d,e)

list_a = [1,2,"test"]
a,b,c= list_a
print(a,b,c)

"""
解题思路 ： 
    任何的序列（或者是可迭代对象）可以通过一个简单的赋值操作来分解为单独的变量。
    唯一的要求就是变量的总数和结构必须与序列相吻合

    总结来说 ： 一个数组或者元组，反正就是一个可以迭代的对象, 都可以进行赋值的操作来分解，或者遍历它，
    唯一的要求是 需要赋值的变量要 和 序列的元素 要吻合 
"""

# 不仅只是元组，数组可以分解， 只要是可以迭代的对象都可以进行分解, 比如 字符串 ， 文件对象
str_a = 'Hello'
for st in str_a:
    print(st)
    pass
h,e,l,l,o = str_a
print(h,e,l,l,o)

# 有时候，你可能只想解压一部分，丢弃其他的值。对于这种情况 Python 并没有提供特殊的语法。 
# 但是你可以使用任意变量名去占位，到时候丢掉这些变量就行了。

data = [ (1,2,3), 'test', 90.1 , 21]
_, test , folat_number,_ = data    # 把不需要的值给丢弃，打印需要的数据
print(test,folat_number)