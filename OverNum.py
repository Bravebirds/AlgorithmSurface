# -*- coding:utf-8 -*-
#!/usr/bin/env python 3.7
# Python version 2.7.16 or 3.7.6
'''
# FileName： OverNum.py
# Author : MrYu
# Desc: PyCharm
# Date： 2021/1/6 22:25
'''
# 有四个数字：1、2、3、5，能组成多少个互不相同且无重复数字的三位数？各是多少？
def get_sum(num):
    result = []
    for i in range(1,num):
        for j in range(1,num):
            if( i != num ) and (i != j) and (j != num):
                result.append("%s%s%s"%(i,num,j))
    return result

print(get_sum(5))