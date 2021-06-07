# -*- encoding: utf-8 -*-
'''
@File    :   15_二进制中1的个数.py
@Time    :   2021/04/28 16:42:09
@Author  :   Dai Zhipeng
@Version :   1.0
@Contact :   ziyao2522@outlook.com
@Desc    :   None
'''

# here put the import lib
class Solution:
    def hammingWeight1(self, n: int) -> int:
        # 根据与运算的定义，二进制数n&1的结果为n最右一位（无符号）
        # Python中与或非运算貌似都是先换算成二进制数
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res
    
    def hammingWeight2(self, n: int) -> int:
        # 使用Python自带库bin，bin处理的二进制数会有0b前缀
        # 可以用slice去掉 [2:]
        return bin(n).count('1')

solution = Solution()
print(bin(int('110000000010000000', 2)))