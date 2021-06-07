# -*- encoding: utf-8 -*-
'''
@File    :   14_剪绳子.py
@Time    :   2021/04/27 17:18:07
@Author  :   Dai Zhipeng
@Version :   1.0
@Contact :   ziyao2522@outlook.com
@Desc    :   https://leetcode-cn.com/problems/jian-sheng-zi-lcof
思路：
1、从常识出发，应该将绳子等分，找到等分能实现最大值的长度为3（贪心算法）
2、动态规划
'''

class Solution:
    def cuttingRope_dp(self, n: int) -> int:
        # dp[i]表示长度为i的绳子剪成m段之后的最大乘积
        dp = [0] * (n + 1)
        # dp[0]等于不减，dp[1]剪了不会让乘积有变化，最小为dp[2]
        dp[2] = 1
        # 绳子总长度最小为2，2的结果直接指定，>=3则进入循环
        for i in range(3, n + 1):
            # j 为要剪的长度
            for j in range(2, i):
                # 剪了第一段之后，剩下的 i-j 可剪可不剪。不剪长度乘积为 j*(i-j)，剪的长度乘积为 j*dp[i-j]
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))
        return dp[n]

