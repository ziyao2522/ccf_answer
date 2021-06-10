# -*- encoding: utf-8 -*-
"""
@File   :   25_合并两个排序列表.py
@Time   :   2021/6/8 16:54
@Desc   :   https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/
@Others :   双指针双指针
"""


class ListNode:
    def __init__(self):
        self.val = None
        self.next = None


class ListNodeHandle:
    def __init__(self):
        self.cur_node = None

    def add(self, x):
        node = ListNode()
        node.val = x
        node = node.next
        return node
        # node.next = self.cur_node
        # self.cur_node = node
        # return node

    def print_ListNode(self, node):
        while node:
            print(1)
            print('\nnode: ', node, ' value: ', node.val, ' next: ', node.next)
            node = node.next


class Solution:
    def merge_sorted_list(self, l1: ListNode, l2: ListNode) -> ListNode:
        # dum作为cur的伪头节点
        cur = dum = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        # 一个ListNode结束之后，剩余节点连上去
        cur.next = l1 if l1 else l2
        return dum.next
