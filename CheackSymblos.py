# -*- coding:utf-8 -*-
#!/usr/bin/env python 3.7
# Python version 2.7.16 or 3.7.6
'''
# FileName： CheackSymblos.py
# Author : MrYu
# Desc: 符号效验
# Date： 2021/1/6 21:58
'''
# 给一个字符串，字符串里有 （）{}[]“”这六个符号，设计一个算法,判断这些符号是否成对匹配
def check_symblos(keyword):
    symblos = {'}': '{', ']': '[', ')': '(', '>': '<'}
    symblos_l, symblos_r = symblos.values(), symblos.keys()
    print("左边括号包含：%s，右边括号包含%s则正确" % (symblos_l, symblos_r))
    symblos_list = []
    for index in range(len(keyword)):
        if keyword[index] in symblos_l:
            symblos_list.append(keyword[index])
        elif keyword[index] in symblos_r:
            if symblos_list and symblos_list[-1] == symblos[keyword[index]]:
                symblos_list.pop()
            else:
                return False
print(check_symblos("3 * {3 +[[(2 -3)] * [5*[[[+5]]}"))