# -*- encoding: utf-8 -*-
'''
@File    :   05_替换空格.py
@Time    :   2021/04/20 16:00:09
@Author  :   Dai Zhipeng
@Version :   1.0
@Contact :   ziyao2522@outlook.com
@Desc    :   https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/
'''

import unittest


class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ', '%20')

class TestMyFunc(unittest.TestCase):
    '''测试类
    '''
    def setUp(self):
        print('准备环境')

    def tearDown(self):
        print('环境清理')
    
    def test_replace_space(self):
        print('开始测试')
        solution = Solution()
        self.assertEqual('12%203', solution.replaceSpace('12 3'))

if __name__ == '__main__':

    # 单纯使用测试用例
    unittest.main()

    # 使用TestSuite控制用例执行顺序
    tests = [TestMyFunc('test_replace_space')]
    suite = unittest.TestSuite()
    suite.addTests(tests)

    runner = unittest.TextTestRunner()
    runner.run(suite)
