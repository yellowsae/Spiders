# 1.3 保留最后 N 个元素

"""
问题
在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？
"""
from collections import deque 

# 使用 deque(maxlen=N) 构造函数会新建一个固定大小的队列。当新的元素加入并且这个队列已满的时候， 最老的元素会自动被移除掉。

q = deque(maxlen=3)  # <class 'collections.deque'>
q.append(1)
q.append(2)
q.append(2)
print(q)
q.append(4)
print(q)
q.append(5)
q.append(6)
print(q)

"""
解决方案
保留有限历史记录正是 collections.deque 大显身手的时候。
比如，下面的代码在多行上面做简单的文本匹配， 并返回匹配所在行的最后N行
"""