'''
1.6. 数字9
【问题描述】
在1至2019中，有多少个数的数位中包含数字9？
注意，有的数中的数位中包含多个9，这个数只算一次。例如，1999这个数包含数字9，在计算只是算一个数。
【答案提交】
这是一道结果填空的题，你只需要算出结果后提交即可。本题的结果为一个整数，在提交答案时只填写这个整数，填写多余的内容将无法得分。
'''


def is_number(num):
    ''' 判断是否有9 '''
    one = num % 10 
    ten = num // 10 % 10 
    hundred = num // 100 % 10 
    thousand = num // 1000 % 10 
    if 9 in [one , ten , hundred, thousand ]:
        return True 
    else:
        False 


number = 2019 

cont = 0 
for i in range(1, number + 1) :
    if is_number(i):
        cont += 1 

print(cont)