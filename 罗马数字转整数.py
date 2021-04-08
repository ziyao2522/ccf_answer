# -*- encoding: utf-8 -*-
'''
@File    :   罗马数字转整数.py
@Time    :   2021/04/06 10:15:33
@Author  :   Dai Zhipeng
@Version :   1.0
@Contact :   ziyao2522@outlook.com
@Desc    :   None
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for i in range(len(s) - 1):
            if roman_dict[s[i]] >= roman_dict[s[i + 1]]:
                result += roman_dict[s[i]]
            else:
                result -= roman_dict[s[i]]
        result += roman_dict[s[-1]]
        return result