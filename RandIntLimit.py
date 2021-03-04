# -*- coding:utf-8 -*-
#!/usr/bin/env python 3.7
# Python version 2.7.16 or 3.7.6
'''
# FileName： RandIntLimit.py
# Author : MrYu
# Desc: PyCharm
# Date： 2021/1/6 22:55
'''

# 生成N个1到1000之间的随机整数（N≤1000）
# 对于其中重复的数字，只保留一个
# 把其余相同的数去掉，不同的数对应着不同的学生的学号
# 然后再把这些数从小到大排序
import random
def get_random(start,end,num):
    if type(start) ==int and type(end) == int:
        number = []
        for i in range(num): # 控制数量
            rand_num = random.randint(start, end)
            if  rand_num not in number:
                number.append(rand_num)
        # 冒泡排序
        for i in range(len(number)):
            for j in range(len(number)-i-1):
                if number[j]>number[j+1]:
                    number[j],number[j + 1] =number[j+1],number[j]
        return number
    else:
        return False

print(get_random(1, 100, 8))