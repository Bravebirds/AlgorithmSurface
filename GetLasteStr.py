# -*- coding:utf-8 -*-
#!/usr/bin/env python 3.7
# Python version 2.7.16 or 3.7.6
'''
# FileName： GetLasteStr.py
# Author : MrYu
# Desc: PyCharm
# Date： 2021/2/27 10:08
'''
# 去掉空格取出最后一组数
def count_str(word):
    split_str = word.split(" ")
    return len(split_str[-1])
print(count_str("hello nowcoder aaa bbb ccc b"))
