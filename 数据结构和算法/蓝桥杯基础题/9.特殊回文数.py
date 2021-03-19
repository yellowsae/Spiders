
"""
资源限制
时间限制：1.0s   内存限制：512.0MB
问题描述
　　123321是一个非常特殊的数，它从左边读和从右边读是一样的。
　　输入一个正整数n， 编程求所有这样的五位和六位十进制数，满足各位数字之和等于n 。
输入格式
　　输入一行，包含一个正整数n。
输出格式
　　按从小到大的顺序输出满足条件的整数，每个整数占一行。
样例输入
52
样例输出
899998
989989
998899
数据规模和约定
　　1<=n<=54。
"""

# 回文数 :  123321  

# 分析 ：  输入n ， 求回文数 ， 回文数在5位和六位数之间 ， 并且 回文数每一位加起来等于 n  , 求出的回文数按大到小排序 


def isNum(num):
    # 判断是否是 回文数 
    num = str(num)  # "123321"
    if num == num[::-1]:    # 这里进行判断 是否是回文数  
        return True
    else:
        return False
    
def sum_num(num):
    # 将回文数的个数都加起来 
    sum = 0  # 初始化
    num = str(num)
    for i in range(len(num)):
        sum += int(num[i])
    return sum  # 返回回文数加起来的和
if __name__ == "__main__":
    n = int(input())
    for num in range(10000,1000000): # 五位到六位数之间
        if isNum(num) and sum_num(num) == n:    #  True and n  -->  n ,  这里判断是否等于 n 
            print(num)


"""
>>> True and 3242
3242 == n 
>>> False and 132

"""

"""
# 分析 ：  输入n ， 求回文数 ， 回文数在5位和六位数之间 ， 并且 回文数每一位加起来等于 n  , 求出的回文数按大到小排序 

心得 ： 先进行回文数在5位和六位数之间  100000 ~ 999999 , 用在循环n 上  for num in ranger(10000,1000000)
        调用函数进行回文数的判断 
                num = str(num)  , is num == num[::-1] 使用切片进行回文数的判断
        调用函数进行 回文数 的求和 
                str(num) 将回文数序列化， 然后循环求 回文数的没位数和 
        
        判断回文数每一位加起来等于 n 
            调用回来的 判断是否是回文数（True） and  返回的求和 == n 
        
        最后输出 
"""
