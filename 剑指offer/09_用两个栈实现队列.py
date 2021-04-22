# -*- encoding: utf-8 -*-
'''
@File    :   09_用两个栈实现队列.py
@Time    :   2021/04/22 17:54:13
@Author  :   Dai Zhipeng
@Version :   1.0
@Contact :   ziyao2522@outlook.com
@Desc    :   None
'''

# here put the import lib


class CQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []


    def appendTail(self, value: int) -> None:
        self.stack_in.append(value)


    def deleteHead(self) -> int:
        if not self.stack_out:
            if not self.stack_in:
                return None
            else:
                while self.stack_in:
                    self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(1)
# obj.appendTail(2)
# obj.appendTail(3)
# param_2 = obj.deleteHead()
# param_2 = obj.deleteHead()
# print(1)