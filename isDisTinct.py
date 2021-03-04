# -*- coding:utf-8 -*-
#!/usr/bin/env python 3.7
# Python version 2.7.16 or 3.7.6
'''
# FileName： isDisTinct.py
# Author : MrYu
# Desc: 实现一个算法：识别一个字符串中，是否包含唯一的字符。
# Date： 2021/1/6 21:59
'''
def assert_distinct(str):
    return len(set(str)) == len(str)
print(assert_distinct("aaaaaabbbbbb"))