# -*- encoding: utf-8 -*-
"""
@File   :   有效的括号.py
@Time   :   2021/6/10 8:11 下午
@Desc   :   https://leetcode-cn.com/problems/valid-parentheses/
@Others :   括号匹配这种要善用栈，python中栈可以用list()生成
"""


class Solution:
    def is_valid(self, s: str) -> bool:
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                else:
                    stack.append(ch)
        return not stack
