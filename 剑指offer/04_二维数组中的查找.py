# -*- encoding: utf-8 -*-
'''
@File    :   04_二维数组中的查找.py
@Time    :   2021/04/20 15:55:06
@Author  :   Dai Zhipeng
@Version :   1.0
@Contact :   ziyao2522@outlook.com
@Desc    :   https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
'''

import collections


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        vertical_size = len(matrix)
        if vertical_size == 0:
            return False
        horizontal_size = len(matrix[0])
        i = horizontal_size - 1
        j = 0
        while i >= 0 and j < vertical_size:
            if target == matrix[j][i]:
                return True
            elif target > matrix[j][i]:
                j += 1
            elif target < matrix[j][i]:
                i -= 1
        return False
