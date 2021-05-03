'''
找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 

'''

'''
0 ～ n-1 范围内的数，分别还原到对应的位置上，如：数字 2 交换到下标为 2 的位置。

若交换过程中发现重复，则直接返回。
'''

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i , num in enumerate(nums):
            while i != num:     # 当数组下标 不等于 数据时 
                if num == nums[num]:   # 数据 等于   数组[数据] 
                    return num          # 有重复就返回 
                nums[i],nums[num] = nums[num], nums[i]  # 当没有重复时    数组[i], 数组[数据] 呼唤 
                num = nums[i]         #  数据 = 数组[下标]， 重新进入循环 
        return -1 


''' 
i :   0  1  2 
num : 2  3  1 

for i num in enumerate(nums):
    当 0 != 2  
        if 2 == 数组[2]:
            返回  2 
        数组[0], 数组[2] = 数组[2], 数组[0]
        num = 数组[0] 
    return -1 

'''