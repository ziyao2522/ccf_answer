# -*- encoding: utf-8 -*-
'''
@File    :   字符串算数运算.py
@Time    :   2021/04/06 15:58:42
@Author  :   Dai Zhipeng
@Version :   1.0
@Contact :   ziyao2522@outlook.com
@Desc    :   None
'''

import re


class Solution:
    def string_arithmetical_operation(self, str: str):
        result = ''
        for i, letter in enumerate(str):
            if letter != '*':
                result += letter
            else:
                new_string = str[i + 2: -1]
                break
        num = int(re.sub(r'\D', '', result))
        var = ''.join(re.findall(r'[A-Za-z]', result))
        iter_string = ''
        if '[' in new_string:
            iter_string = Solution().string_arithmetical_operation(new_string)
            return var + iter_string * num
        else:
            return var + new_string * num

solution = Solution()
print(solution.string_arithmetical_operation('3*[a2*[c]]'))
