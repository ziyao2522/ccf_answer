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
        # return s.replace(' ', '%20')
        original_length = len(s)
        blank_number = 0
        for i in s:
            if i == ' ':
                blank_number += 1
        new_length = original_length + blank_number * 2
        origin_index = original_length - 1
        result_index = new_length - 1
        result_string = s + ' ' * 2 * blank_number
        while origin_index >= 0:
            if s[origin_index] == ' ':
                result_string[result_index] = '0'
                result_string[result_index - 1] = '2'
                result_string[result_index - 2] = '%'
                result_index -= 3
            else:
                result_string[result_index] = s[origin_index]
                result_index -= 1
            origin_index -= 1
        return result_string
        

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
        self.assertEqual('123%20', solution.replaceSpace('123 '))

if __name__ == '__main__':

    # 单纯使用测试用例
    unittest.main()

    # 使用TestSuite控制用例执行顺序
    tests = [TestMyFunc('test_replace_space')]
    suite = unittest.TestSuite()
    suite.addTests(tests)

    runner = unittest.TextTestRunner()
    runner.run(suite)
