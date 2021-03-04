# -*- coding:utf-8 -*-
#!/usr/bin/env python 3.7
# Python version 2.7.16 or 3.7.6
'''
# FileName： DeleteStr.py
# Author : MrYu
# Desc: PyCharm
# Date： 2021/2/27 10:00
'''
# 删除字符串a中包含的字符串b，举例 输入a = "asdw",b = "sd" 返回 字符串 “aw”，并且测试这个程序
def delect_str(keyword,del_value):
    print(str(keyword).replace(del_value,""))
delect_str("asdw","sd")
