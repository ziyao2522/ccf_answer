# -*- encoding: utf-8 -*-
"""
@File    :   13_机器人的运动范围.py
@Time    :   2021/04/25 18:19:09
@Author  :   Dai Zhipeng
@Version :   1.0
@Contact :   ziyao2522@outlook.com
@Desc    :   https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/
广度优先搜索查路径，外加障碍排除
"""

from queue import Queue


def digit_sum(n):
    res = 0
    while n:
        res += n % 10
        n //= 10
    return res


class Solution:
    @staticmethod
    def moving_count(self, m: int, n: int, k: int) -> int:
        q = Queue()
        q.put((0, 0))
        # set()为无序不重复元素集
        s = set()
        while not q.empty():
            x, y = q.get()
            if (x, y) not in s and 0 <= x < m and 0 <= y < n and digit_sum(x) + digit_sum(y) <= k:
                s.add((x, y))
                # 这个循环实际上就是将x0, y0分别赋为括号1和括号2的值
                for x0, y0 in [(x + 1, y), (x, y + 1)]:
                    q.put(x0, y0)
        return len(s)