# -*- encoding: utf-8 -*-
"""
@File   :   27_二叉树的镜像.py
@Time   :   2021/6/9 18:00
@Desc   :   https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/
@Others :   镜像就是交换所有节点的左右节点。二叉树多用递归解决问题。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirror_tree1(self, root: TreeNode) -> TreeNode:
        # 递归法，二叉树常用操作方法
        temp = root.left
        root.left = self.mirror_tree1(root.right)
        root.right = self.mirror_tree1(temp)
        return root
    def
