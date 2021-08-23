
"""
资源限制
时间限制：1.0s   内存限制：512.0MB
问题描述
　　1221是一个非常特殊的数，它从左边读和从右边读是一样的，编程求所有这样的四位十进制数。
输出格式
　　按从小到大的顺序输出满足条件的四位十进制数。
"""


# 分析 ：  求四位数的所有回文数  ranger(1000,10000)

def isNumber(num):
    num = str(num)  # 将数字序列化
    if num == num[::-1]:    # 这里判断回文数
        return True
    else:
        return False
if __name__ == "__main__":
    for num in range(1000,10000):   # 所有的四位数 
        if isNumber(num) :
            print(num)

# 心得 ：因为上一题的 学到 回文数的判断，和位数的判断 ， 所以做这题没有压力 
# 