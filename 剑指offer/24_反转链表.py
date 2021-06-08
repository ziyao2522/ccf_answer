# -*- encoding: utf-8 -*-
"""
@File   :   24_反转链表.py
@Time   :   2021/6/8 15:57
@Desc   :   https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/
@Others :   双指针可解，利用双指针和中间变量将两个节点间的指针反转，最后返回双指针中的一个即可
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverse_list(self, head: ListNode) -> ListNode:
        # pre为前一指针，cur为后一指针
        cur = head
        pre = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
