# -*- encoding: utf-8 -*-
'''
@File    :   字符串命名转换.py
@Time    :   2021/04/06 15:20:35
@Author  :   Dai Zhipeng
@Version :   1.0
@Contact :   ziyao2522@outlook.com
@Desc    :   None
'''

# here put the import lib
class Solution:
    def string_name_chanage(self, s: str):
        type1_string = ''
        type2_string = ''
        type3_string = ''
        type4_string = ''
        sign = False
        type1_string += (s[0].upper())
        type2_string += (s[0].lower())
        type3_string += (s[0].lower())
        type4_string += (s[0].lower())
        for i in range(1, len(s)):
            if s[i].isupper() or sign:
                type1_string += (s[i].upper())
                type2_string += (s[i].upper())
                if not sign:
                    type3_string += ('_')
                type3_string += (s[i].lower())
                if not sign:
                    type4_string += ('-')
                type4_string += (s[i].lower())
                sign = False
            elif (s[i] == '_' or s[i] == '-'):
                type3_string += ('_')
                type4_string += ('-')
                sign = True
            else:
                type1_string += (s[i])
                type2_string += (s[i])
                type3_string += (s[i])
                type4_string += (s[i])
                sign = False
        print('{} {} {} {}'.format(type1_string, type2_string, type3_string, type4_string))

solution = Solution()
solution.string_name_chanage('AppBppCpp')