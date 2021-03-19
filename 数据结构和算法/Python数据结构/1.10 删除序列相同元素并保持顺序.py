
# 怎样在一个序列上面保持元素顺序的同时消除重复的值？

# 使用 dedupe() 函数 对list 类型的  相同数据进行去重 
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))

# 简答去除重读的数据
# a = {1, 5, 2, 1, 9, 1, 5, 10}
a = set(a)  # 将 list 转为 set 
print(sorted(a))  # sorted() 进行排序

# 总结 ：  set()  集合能自动的去重 , 如果需要进行排序 使用排序函数 sorted() 就行