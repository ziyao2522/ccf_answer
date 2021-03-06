# -*- encoding: utf-8 -*-
'''
@File    :   algorithm_sort.py
@Time    :   2021/04/12 17:13:28
@Author  :   Dai Zhipeng
@Version :   1.0
@Contact :   ziyao2522@outlook.com
@Desc    :   None
'''

# here put the import lib


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, left, right):
    pivot = left
    index = pivot + 1
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index += 1
        i += 1
    swap(arr, i, index-1)
    return index - 1


class Sort:
    def insertion_sort(self, arr):
        for i in range(len(arr)):
            pre_index = i - 1
            current_value = arr[i]
            while pre_index >= 0 and arr[pre_index] > current_value:
                arr[pre_index + 1] = arr[pre_index]
                pre_index -= 1
            arr[pre_index + 1] = current_value
        return arr

    def bubble_sort(self, arr):
        for i in range(1, len(arr)):
            for j in range(0, len(arr) - i):
                if arr[j + 1] < arr[j]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j] # Python可以实现无中间变量交换数值
        return arr
    
    def quick_sort(self, arr, left=None, right=None):
        



if __name__ == '__main__':
    sort = Sort()
    sort.insertion_sort([3, 4, 1, 2])