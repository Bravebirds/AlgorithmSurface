# -*- coding:utf-8 -*-
#!/usr/bin/env python 3.7
# Python version 2.7.16 or 3.7.6
'''
# FileName： OddToEven.py
# Author : MrYu
# Desc: PyCharm
# Date： 2021/1/6 22:10
'''
# 判断xxx区间有多少个奇数和偶数
def su_num(start,end):
    odd_num = []
    even_num = []
    for i in range(start,end):
        if i %2!=0:
            odd_num.append(i)
        elif i!=0:
            even_num.append(i)
    return {"odd":odd_num,"even":even_num}

print(su_num(1,200))

