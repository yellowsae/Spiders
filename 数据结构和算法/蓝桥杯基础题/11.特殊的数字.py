"""
问题描述
　　153是一个非常特殊的数，它等于它的每位数字的立方和，即153=1*1*1+5*5*5+3*3*3。编程求所有满足这种条件的三位十进制数。
输出格式
　　按从小到大的顺序输出满足条件的三位十进制数，每个数占一行。

"""

# 分析 ： 求 一个数字 等于它的每位数字的 立方和 ， 满足这种条件的三位十进制数 


def isNumber(num):
    # num = str(num) 
    sum = pow(int(str(num)[0]),3) + pow(int(str(num)[1]),3) + pow(int(str(num)[2]),3)   # 进行三次方相乘 
    if num == sum:
        return True
    else:
        return False
        
if __name__ == "__main__":
    for num in range(100,1000): # 三位数 
        if isNumber(num) :
            print(num)


"""
学到了  pow() 函数的使用  ， pow() 方法返回 xy（x 的 y 次方） 的值。
pow(2,3) --> 2 * 2 * 2 
"""

# 第二种方法 
def isNum(num):
    a = num % 10    # 153 % 10  --> 3 
    b = (num // 10) % 10    # 153 // 10 = 15  , 15 % 10 = 5  
    c = (num // 100 ) % 10   #  153 // 100 = 1  ， 1 % 10 = 1 
    if num == pow(a,3) + pow(b,3) + pow(c,3):
        return True

if __name__ == '__main__':
    for num in range(100,10000):
        if isNum(num):
            print(num)

"""
心得 ： pow(2,3) --> 2 * 2 * 2 
    学到了 对数字的处理 , 取余操作， 分解大数 中 的 每一位数 
"""