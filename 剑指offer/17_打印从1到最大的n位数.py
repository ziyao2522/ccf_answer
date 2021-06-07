# -*- encoding: utf-8 -*-
"""
@File   :   17_打印从1到最大的n位数.py
@Time   :   2021/6/7 4:01 下午
@Desc   :   
@Others :   
"""

class Solution:
    def print_numbers(self, n: int) -> List[int]:
        upper_num = pow(10, n) - 1
        res_list = []
        for i in range(1, upper_num):
            res_list.append(i)