
# 给一个整数 n  找到若干个完全平方数 (1 , 4, 9 ) ，使得它们的和 等于 n ， 完全平方数的个数最少 

# 问题示例 
# 
#  n = 12  ， 返回 3  , 因为 12 = 4 + 4 + 4 ; 
#  n = 13  , 返回 2  ， 13 = 4 + 9 

class Solution(object):
	def numSquares(self,n):
		while n % 4 == 0 :	# 12 % 4 == 0 
			#  // 取整  除 ，向下取整 
			n //= 4 	# 12 // 4 = 3 

		if n % 8 == 7:	# 12 % 8 = 4 
			return 4 

		for i in range(n + 1) :
			temp =  i * i 
			if temp <= n:
				if int(( n - temp) ** 0.5 ) ** 2 + temp == n :
					return 1 + ( 0 if temp == 0 else 1 )
				else:
					break
		return 3 


if __name__ == '__main__':
	n = 12 
	solution = Solution()
	print(solution.numSquares(n))

"""

"""