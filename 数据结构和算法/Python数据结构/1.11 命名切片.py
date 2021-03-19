#  如果你的程序包含了大量无法直视的硬编码切片，并且你想清理一下代码。

record = '....................100 .......513.25 ..........'
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)

print(len(record))


a = slice(2,4,2)
s = 'HelloWorld'
a.indices(len(s))
for i in range(*a.indices(len(s))):
    print(i)