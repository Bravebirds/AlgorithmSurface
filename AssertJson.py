# -*- coding:utf-8 -*-
#!/usr/bin/env python 3.7
# Python version 2.7.16 or 3.7.6
'''
# FileName： AssertJson.py
# Author : MrYu
# Desc: PyCharm
# Date： 2021/2/27 9:05
'''
# 判断俩json是否相等
import operator
import json_tools
keyword = {"id": "100", "name": "苹果","info": {"uid":"2020","phoneName":["一代","Mate40"]}}
keyword1 = {"id": "100","info": {"uid":"2020","phoneName":["一代","Mate40"]}, "name": "苹果"}
# 方法一 调库 若不相等则数组非空
print(json_tools.diff(keyword, keyword1))
# 方法二 递归
def json_clear(keyword,keyword1):
    if type(keyword)==dict and type(keyword1)==dict:
        if len(keyword) == len(keyword1):
            # 优先对比所有的key值是否一致不一致立刻返回结果不走values判断
            keys1 = keyword.keys()
            keys2 = keyword1.keys()
            equal = []
            not_equal = []
            if keys1==keys2:
                list_keys = [i for i in keys1]
                for i in range(len(list_keys)):
                    if keyword[list_keys[i]]==keyword1[list_keys[i]]:
                        equal.append(list_keys[i])
                    else:
                        not_equal.append(list_keys[i])
                return {"equal":equal,"not_equal":not_equal}
            else:
                return "俩数组Key不一致"
        else:
            return "俩长度不一致，A：%s，B：%s"%(len(keyword),len(keyword1))
    elif type(keyword)==list and type(keyword1)==list:
        # 方法一
        return operator.eq(keyword,keyword1)
    else:
        return "type(keyword)!=type(dict(2))"

print(json_clear(keyword, keyword1))
