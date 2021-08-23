
# # 分析 ：  输入n ， 求回文数 ， 回文数在5位和六位数之间 ， 并且 回文数每一位加起来等于 n  , 求出的回文数按大到小排序 


def isNumber(num):
    # 序列化
    num = str(num)
    # 判断是否 是回文数 
    if num == num[::-1]:
        return True
    else:
        return False 

def is_Sum(num):
    # 序列化 
    num = str(num)
    Sum_x = 0 
    for i in range(len(num)):
        Sum_x += int(num[i])
    return Sum_x
n = int(input())
for num in range(10000,1000000):
    if isNumber(num) and is_Sum(num) == n :
        print(num)