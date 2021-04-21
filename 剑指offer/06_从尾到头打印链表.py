# -*- encoding: utf-8 -*-
'''
@File    :   06_从尾到头打印链表.py
@Time    :   2021/04/21 16:20:50
@Author  :   Dai Zhipeng
@Version :   1.0
@Contact :   ziyao2522@outlook.com
@Desc    :   None
'''

import unittest
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode):
        res_list = []
        while head:
            res_list.append(head.val)
            head = head.next
        return res_list[::-1]

class TestMyFunc(unittest.TestCase):
    '''测试类
    '''
    @classmethod
    def setUp(cls):
        print('准备环境')

    @classmethod
    def tearDown(cls):
        print('环境清理')
    
    def test_replace_space(self):
        print('开始测试')
        solution = Solution()
        node_list = ListNode(1)
        self.assertEqual([1, 2, 3], solution.reversePrint(node_list))

if __name__ == '__main__':

    # 单纯使用测试用例
    unittest.main()