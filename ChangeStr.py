# -*- coding:utf-8 -*-
#!/usr/bin/env python 3.7
# Python version 2.7.16 or 3.7.6
'''
# FileName： ChangeStr.py
# Author : MrYu
# Desc: 反转字符串中的字符
# Date： 2021/2/27 9:55
'''
def change_str(chars):
    size = len(chars)
    for i in range(size//2):
        chars[i],chars[size-1-i] = chars[size-1-i],chars[i]
    return chars

print(change_str(['b', ' ','aaa', 'a', 'r']))