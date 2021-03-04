# -*- coding:utf-8 -*-
#!/usr/bin/env python 3.7
# Python version 2.7.16 or 3.7.6
'''
# FileName： ReturnStr.py
# Author : MrYu
# Desc: PyCharm
# Date： 2021/1/6 23:05
'''
# 给定一个整数 num，从 1 到 num 按照下面的规则返回每个数：
# 如果这个数被 3 整除，返回 'Fizz'。
# 如果这个数被 5 整除，返回 'Buzz'。
# 如果这个数能同时被 3 和 5 整除，返回 'FizzBuzz'。
# 如果这个数既不能被 3 也不能被 5 整除，返回这个数字的字符串格式。
def return_rule(num):
    relust = []
    for i in range(1,num):
        if i % 3 == 0:
            relust.append("Fizz")
        elif i % 5 == 0:
            relust.append("Buzz")
        elif i %3==0 and i%5==0:
            relust.append("FizzBuzz")
        elif i%3 !=0 and i%5!=0:
            relust.append(i)
    return relust

print(return_rule(100))