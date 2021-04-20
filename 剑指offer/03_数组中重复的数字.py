# -*- encoding: utf-8 -*-
'''
@File    :   03_数组中重复的数字.py
@Time    :   2021/04/20 15:58:06
@Author  :   Dai Zhipeng
@Version :   1.0
@Contact :   ziyao2522@outlook.com
@Desc    :   https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
'''

# here put the import lib
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        count_list = [0] * len(nums)
        for i in range(len(nums)):
            count_list[i] = 0
        for i in range(len(nums)):
            if count_list[nums[i]] == 1:
                print(nums[i])
                break
            else:
                count_list[nums[i]] = 1
