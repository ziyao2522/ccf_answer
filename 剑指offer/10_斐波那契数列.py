# -*- encoding: utf-8 -*-
'''
@File    :   10_斐波那契数列.py
@Time    :   2021/04/23 10:38:19
@Author  :   Dai Zhipeng
@Version :   1.0
@Contact :   ziyao2522@outlook.com
@Desc    :   动态规划
'''

# here put the import lib
class Solution:
    def fib(self, n: int) -> int:
        dp = []
        dp.append(0)
        dp.append(1)
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            for i in range(2, n + 1):
                dp_temp = dp[i - 1] + dp[i - 2]
                dp.append(dp_temp)
        return dp[n]

solution = Solution()
print(solution.fib(100000))