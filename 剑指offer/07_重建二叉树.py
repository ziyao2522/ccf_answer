# -*- encoding: utf-8 -*-
'''
@File    :   07_重建二叉树.py
@Time    :   2021/04/22 14:27:13
@Author  :   Dai Zhipeng
@Version :   1.0
@Contact :   ziyao2522@outlook.com
@Desc    :   https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/
思路：前序遍历第一个元素为根节点。在中序遍历中找到根节点，则可以将中序遍历序列分割为左、根、右，得到三树的
节点数。根据节点数，将前序遍历分割为根，左，右。递归
'''

# here put the import lib


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:
        def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            '''
            @param: 均为节点在遍历中的索引
            '''
            if preorder_left > preorder_right:
                return None
            
            # 前序遍历中的第一个节点就是根节点
            preorder_root = preorder_left
            # 中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]

            # 建立根节点
            root = TreeNode(preorder[preorder_root])
            # 得到左子树中的节点数目
            size_left_subtree = inorder_root - inorder_left
            # 递归构造左子树，并连接到根节点
            # 先序遍历中“从 左边界+1 开始的 size_left_subtree” 个元素对应了中序遍历中“从 左边界 开始到 根节点定位-1”的元素
            root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
            # 先序遍历中“从 左边界+1+左子树节点数目 开始到 右边界”的元素对应了中序遍历中“从 根节点定位+1 到 右边界”的元素
            root.right = myBuildTree(preorder_left + 1 + size_left_subtree, preorder_right, inorder_root + 1, inorder_right)
            return root

        n = len(preorder)
        # 构建中序遍历的哈希映射，定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)