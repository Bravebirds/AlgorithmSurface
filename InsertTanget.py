# -*- coding:utf-8 -*-
#!/usr/bin/env python 3.7
# Python version 2.7.16 or 3.7.6
'''
# FileName： InsertTanget.py
# Author : MrYu
# Desc: PyCharm
# Date： 2021/3/5 0:09
'''
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
# 如果目标值不存在于数组中，返回它将会被按顺序插入的位置
# 你可以假设数组中无重复元素。
def find_index(lists,tangent):
    if type(lists) is not list:
        return False
    else:
        if tangent < lists[0]:
            return 0
        elif tangent >= lists[len(lists) - 1]:
            return len(lists)
        else:
            for i in range(len(lists)):
                if tangent == lists[i]:
                    return i
                elif tangent >lists[i] and tangent<=lists[i+1]:
                    return i+1
            # return lists.index(tangent)
print(find_index([1, 3, 5, 6], 5))