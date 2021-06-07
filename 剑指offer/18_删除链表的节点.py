# -*- encoding: utf-8 -*-
"""
@File   :   18_删除链表的节点.py
@Time   :   2021/6/7 4:17 下午
@Desc   :   
@Others :   
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    @staticmethod
    def delete_node(self, head: ListNode, val: int) -> ListNode:
        # 删除head的情况
        if head.val == val:
            return head.next
        # 指定当前节点pre和指向节点cur
        pre, cur = head, head.next
        # 下一节点存在且不是目标节点，则指针向下移动
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        pre.next = cur.next
        return head
