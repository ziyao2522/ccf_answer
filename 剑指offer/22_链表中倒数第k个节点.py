# -*- encoding: utf-8 -*-
"""
@File   :   22_链表中倒数第k个节点.py
@Time   :   2021/6/8 15:37
@Desc   :   https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof
@Others :   思路1、统计链表长度n找到n-k即可  思路二，双指针，两个指针初始都在头节点，后面的指针运动k步后，两个指针一起运动到结束，前指针所在位置
即倒数k
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def get_kth_from_end(self, head: ListNode, k: int) -> ListNode:
        former, latter = head, head
        for _ in range(k):
            latter = latter.next
        while latter:
            former = former.next
            latter = latter.next
        return former
