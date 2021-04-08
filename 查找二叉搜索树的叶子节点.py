# -*- encoding: utf-8 -*-
'''
@File    :   查找二叉搜索树的叶子节点.py
@Time    :   2021/04/07 13:57:59
@Author  :   Dai Zhipeng
@Version :   1.0
@Contact :   ziyao2522@outlook.com
@Desc    :   给出二叉搜索树的前序遍历，输出所有叶子节点
'''

# here put the import lib
class Solution:
    def search_binary_search_tree_leaves(self, nums: []):
        if len(nums) == 1:
            return nums
        result = []
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                result.append(nums[i - 1])
        result.append(nums[-1])
        return result

solution = Solution()
print(solution.search_binary_search_tree_leaves([15, 10, 6, 12, 20, 16, 24]))