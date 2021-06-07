# -*- encoding: utf-8 -*-
'''
@File    :   13_机器人的运动范围.py
@Time    :   2021/04/25 18:19:09
@Author  :   Dai Zhipeng
@Version :   1.0
@Contact :   ziyao2522@outlook.com
@Desc    :   https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/
'''

from queue import Queue


def digitsum(n):
    res = 0
    while n:
        res += n % 10
        n //= 10
    return res


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        q = Queue()
        q.put((0, 0))
        s = set()
        while not q.empty():
            x, y = q.get()
            if (x, y) not in s and 0 <= x < m and 0 <= y < n and digitsum(x) +  digitsum(y) <= k:
                s.add((x, y))
                for nx, ny in [(x + 1, y), (x, y + 1)]:
                    q.put((nx, ny))
        return len(s)