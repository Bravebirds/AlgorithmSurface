# -*- coding:utf-8 -*-
#!/usr/bin/env python 3.7
# Python version 2.7.16 or 3.7.6
'''
# FileName： GetUgly.py
# Author : MrYu
# Desc: 获取指定值内所有的丑数
# Date： 2021/3/1 22:01
'''
def is_ugly(num: int) -> bool:
    if num < 1:
        return False
    else:
        while True:
            if num % 2 == 0:
                num = num / 2
            if num % 3 == 0:
                num = num / 3
            if num % 5 == 0:
                num = num / 5
            if num % 2 != 0 and num % 3 != 0 and num % 5 != 0:  # 把数字除尽，尽可能地除以2、3、5
                break
        return True if num == 1 else False  # 除尽后如果等于1，代表是丑数，如果不等于1，那就不是丑数了

def get_ugly(num):
    ugly_list = []
    for i in range(num):
        if is_ugly(i) is True:
            ugly_list.append(i)
    return ugly_list

print(is_ugly(1))
print(get_ugly(1000000))