# -*- encoding: utf-8 -*-
'''
@File    :   16_数值的整数次方.py
@Time    :   2021/04/28 17:27:51
@Author  :   Dai Zhipeng
@Version :   1.0
@Contact :   ziyao2522@outlook.com
@Desc    :   https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/
快速幂法
'''

# here put the import lib
def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        res = 1
        if n < 0:
            x = 1/x
            n = -n
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res