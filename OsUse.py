# -*- coding:utf-8 -*-
#!/usr/bin/env python 3.7
# Python version 2.7.16 or 3.7.6
'''
# FileName： OsUse.py
# Author : MrYu
# Desc: PyCharm
# Date： 2021/1/6 22:20
'''
# os模块
import os
head,tail = os.path.split(os.path.dirname(__file__))
file_path ="OsTest.txt"
with open(file_path,encoding="utf-8") as file:
    print(file.read())
    print(os.access(file_path, os.R_OK))
    print(os.access(file_path, os.X_OK))
    print(os.access(file_path, os.W_OK))
file.close()