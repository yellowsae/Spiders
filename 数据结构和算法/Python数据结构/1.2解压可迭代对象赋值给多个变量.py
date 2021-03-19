"""
1.2 解压可迭代对象赋值给多个变量

问题
如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。 那么怎样才能从这个可迭代对象中解压出 N 个元素出来？
"""

list_test = [1,2,3,4,'test']
a,*b,test = list_test  # 可以使用 * 号 代替中间的变量,  此时的带 * 号的变量的类型是一个  list 类型 
print(a,*b,test)
print(b)  # list 

#  此时的 b 是 list 
# 解压出的b变量永远都是列表类型，不管解压的 number 数量是多少（包括 0 个）。
#  所以，任何使用到 number 变量的代码就不需要做多余的类型检查去确认它是否是列表类型了。


"""
Python 的星号表达式可以用来解决这个问题
"""

# 星号表达式也能用在列表的开始部分。 
data = ['test',1,2,3,4]
*str_test,number_test ,number = data
print(*str_test)
print(number_test)
print(number)

# 值得注意的是，星号表达式在迭代元素为可变长元组的序列时是很有用的。 比如，下面是一个带有标签的元组序列：

records = [ ('foot',1,2), ('bar,2,3'),('hello,4,5')]

def foo(x,y):
    print('foot',x,y)

def bar(x,y):
    print('bar',x,y)

for tag, *arge in records:  # 直接循环 元组了
    if tag == 'foot':
        foo(*arge)
    elif tag == 'bar':
        bar(*arge)

# 星号解压语法在字符串操作的时候也会很有用，比如字符串的分割。
list_str = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname,  *filds , homeder, sh = list_str.split(':')  # split('') 以什么的方式进行分割字符串，返回的是 list 类型
print(uname)
print(homeder)
print(sh)

# 有时候，你想解压一些元素后丢弃它们，你不能简单就使用 * ， 
# 但是你可以使用一个普通的废弃名称，比如 _ 或者 ign （ignore）。
record = ('ACME', 50, 123.45, (12, 18, 2012))
name , *num , (*n,year) = record
print(name,year)

# 如果你够聪明的话，还能用这种分割语法去巧妙的实现递归算法。比如：
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

content = sum([2,3])
print(content)
