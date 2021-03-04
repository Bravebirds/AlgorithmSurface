# -*- coding:utf-8 -*-
#!/usr/bin/env python 3.7
# Python version 2.7.16 or 3.7.6
'''
# FileName： LimitPage.py
# Author : MrYu
# Desc: PyCharm
# Date： 2021/1/6 22:07
'''

# 从一个数组中找出前或者后xxxx个数 冒泡?原理用后面的与前一个值比较后替换俩者位置 具体按降序或升序逻辑走
max_list = [18,66,90,55,71,0,6,77,5,1,9,5]
def selete_max():
    for i in range(len(max_list)):
        for j in range(len(max_list)-i-1):
            if max_list[j]>max_list[j+1]:
                max_list[j],max_list[j+1]=max_list[j+1],max_list[j]
    print(max_list[:5]) # 取前多少/默认从0开始
    print(max_list[-6:-1]) # 取后多少/没有默认值
selete_max()