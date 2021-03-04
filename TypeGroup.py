# -*- coding:utf-8 -*-
#!/usr/bin/env python 3.7
# Python version 2.7.16 or 3.7.6
'''
# FileName： TypeGroup.py
# Author : MrYu
# Desc: 字符类型分组
# Date： 2021/1/6 22:08
'''
def count_type(word):
    sapce_list = []
    ascii_list = []
    num_list = []
    str_list =[]
    for i in range(len(word)):
        if word[i].isspace() is True:
            sapce_list.append(word[i])
        elif word[i].islower() is True or word[i].isupper() is True:
            ascii_list.append(word[i])
        elif word[i].isdigit() is True:
            num_list.append(word[i])
        elif word[i].isalnum() is True:
            str_list.append(word[i])
    return {"sapce":len(sapce_list),"asii":len(ascii_list),"num":len(num_list),"str":len(str_list)}
print(count_type("aaa+/*12@!>< -+^&%$$#/*/*/{}】【、085433*())啊哈哈哈啊哈哈哈哈qqjfjfhfQQEWQqwwrff"))
