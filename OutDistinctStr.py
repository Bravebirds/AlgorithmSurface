# -*- coding:utf-8 -*-
#!/usr/bin/env python 3.7
# Python version 2.7.16 or 3.7.6
'''
# FileName： OutDistinctStr.py
# Author : MrYu
# Desc: PyCharm
# Date： 2021/1/6 22:09
'''

# 输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
def dis_tinct(num):
    change_str = str(num)[::-1]  # 反转后的字符串
    answer = []
    for i in change_str:
        if i not in answer:
            answer.append(i)
    return ("".join(answer))

print(dis_tinct(558996885221111992712833887211111565779552222))