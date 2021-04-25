# -*- encoding: utf-8 -*-
'''
@File    :   12_矩阵中的路径.py
@Time    :   2021/04/25 16:52:42
@Author  :   Dai Zhipeng
@Version :   1.0
@Contact :   ziyao2522@outlook.com
@Desc    :   https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof
回溯法，深度优先搜索
'''

# here put the import lib
class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= i < len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            board[i][j] = ''
            res = dfs(i + 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = word[k]
            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False

solution = Solution()
print(solution.exist([['C', 'B'], ['C', 'B']], 'CB'))