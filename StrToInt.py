# -*- coding:utf-8 -*-
#!/usr/bin/env python 3.7
# Python version 2.7.16 or 3.7.6
'''
# FileName： StrToInt.py
# Author : MrYu
# Desc: PyCharm
# Date： 2021/1/6 22:06
'''
# 把字符串转为数字，比如 str="1234"，变成 int 1234
def re_str_type(key):
    int_num = int(key)
    print(int_num,type(int_num))
re_str_type("11111")