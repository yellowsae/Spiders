'''
1.9. 音节判断
【问题描述】
小明对类似于 hello 这种单词非常感兴趣，这种单词可以正好分为四段，第一段由一个或多个辅音字母组成，第二段由一个或多个元音字母组成，第三段由一个或多个辅音字母组成，第四段由一个或多个元音字母组成。
给定一个单词，请判断这个单词是否也是这种单词，如果是请输出yes，否则请输出no。
元音字母包括 a, e, i, o, u，共五个，其他均为辅音字母。
【输入格式】
输入一行，包含一个单词，单词中只包含小写英文字母。
【输出格式】
输出答案，或者为yes，或者为no。
【样例输入】
lanqiao
【样例输出】
yes
【样例输入】
world
【样例输出】
no
【评测用例规模与约定】
对于所有评测用例，单词中的字母个数不超过100。

hello   # e 和 o 是 元音，   在字符串的 1 和 4 的位置 

解题 判断 在字符串的 1 和 4 的位置   是 返回 yes  , 不是 no  

'''


word = input() 

vowel =  [ 'a', 'e' , 'i' , 'o', 'u'] 
i = 0 
ans = 0 

if word[i] in vowel:
    print('no')
else:
    ans += 1 
    i += 1 
    while i < len(word):
        if word[i] not in vowel:
            i +=1 
        else:
            ans += 1 
            print(i,ans)
            break

    while i < len(word):
        if word[i] in vowel:
            i += 1 
        else:
            ans += 1 
            break
    while i < len(word):
        if word[i] in vowel:
            i += 1 
        else:
            ans += 1 
            break
    while i < len(word):
        if word[i] in vowel:
            i += 1 
        else:
            ans += 1 
            break
    if ans == 4 :
        print('yes')
    else:
        print('no')
