# -*- encoding: utf-8 -*-
"""
@File   :   26_树的子结构.py
@Time   :   2021/6/9 11:10
@Desc   :   https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof
@Others :   步骤：1、判断a树中是否有节点为b树的根节点 2、判断以此节点为根节点的子树中是否包含b树
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_sub_structure(self, a: TreeNode, b: TreeNode) -> bool:
        # 判断a，b的左子节点是否相等；右子节点是否相等
        def recur(a: TreeNode, b: TreeNode) -> bool:
            if not b:
                return True
            elif not a or a.val != b.val:
                return False
            return recur(a.left, b.left) and recur(a.right, b.right)
        # 排除a或b为空的情况，剩下三种情况
        # 1、 b以a的根节点为根节点 2、b的根节点在a的left 3、b的根节点在a的right
        return bool(a and b) and (recur(a, b) or self.is_sub_structure(a.left, b) or self.is_sub_structure(a.right, b))
