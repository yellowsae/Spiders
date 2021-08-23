# 怎样找出一个序列中出现次数最多的元素呢？

# collections.Counter 类就是专门为这类问题而设计的， 它甚至有一个有用的 most_common() 方法直接给了你答案。

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter , defaultdict ,deque
word_counts = Counter(words) # 创建对象 
# 出现频率最高的3个单词
top_three = word_counts.most_common(3)
print(top_three)

work_str = str(words)
print(work_str.find('look'))

# 使用 update() 方法 
# print(word_counts.update(words))


# 直接查看出现多少次
print(word_counts['my'])  


# 总结 : 使用 collections.Counter 方法 