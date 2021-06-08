# -*- encoding: utf-8 -*-
"""
@File   :   21_调整数组顺序使技术排在偶数之前.py
@Time   :   2021/6/7 4:17 下午
@Desc   :   https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
@Others :
"""
class Solution:
    def exchange1(self, nums: List[int]) -> List[int]:
        # 双数组法，时间少，空间大
        odd_num = []
        even_num = []
        for i in nums:
            if i % 2 == 0:
                even_num.append(i)
            else:
                odd_num.append(i)
        res = odd_num + even_num
        return res

    def exchange2(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        # 首尾指针标准写法
        while left <= right:
            # 如果左侧指针所指为奇数，则左指针右移一位
            if nums[left] % 2 == 1:
                left += 1
            # 左指针所指为偶数的情况下，如果右指针指向偶数，则右指针左移一位
            elif nums[right] % 2 == 0:
                right -= 1
            # 否则，这两个元素应该调换位置
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return nums
