# -*- encoding: utf-8 -*-
'''
@File    :   10_青蛙跳台阶.py
@Time    :   2021/04/23 11:06:26
@Author  :   Dai Zhipeng
@Version :   1.0
@Contact :   ziyao2522@outlook.com
@Desc    :   https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/
理解：当跳上1个台阶之后，还剩n-1个台阶可以调。当跳上2个台阶之后，还剩n-2个台阶可以跳。抽象成递归问题，用动态规划解决
'''

# here put the import lib
class Solution:
    def numWays(self, n: int) -> int:
        dp = []
        dp.append(1)
        dp.append(1)
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            for i in range(2, n + 1):
                dp_temp = dp[i - 1] + dp[i - 2]
                dp.append(dp_temp % 1000000007)
        return dp[n]