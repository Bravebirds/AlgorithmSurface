# -*- coding:utf-8 -*-
#!/usr/bin/env python 3.7
# Python version 2.7.16 or 3.7.6
'''
# FileName： BigPass.py
# Author : v_yanqyu
# Desc: PyCharm
# Date： 2021/3/3 9:49
'''
import operator
import os
import random
import json_tools



# 实现一个算法：识别一个字符串中，是否包含唯一的字符。
def assert_distinct(str):
    return len(set(str)) == len(str)
print(assert_distinct("aaaaaabbbbbb"))

# 反转字符串中的字符
def change_str(chars):
    size = len(chars)
    for i in range(size//2):
        chars[i],chars[size-1-i] = chars[size-1-i],chars[i]
    return chars

print(change_str(['b', ' ','aaa', 'a', 'r']))


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

# 获取指定值内所有的丑数
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

# 有四个数字：1、2、3、5，能组成多少个互不相同且无重复数字的三位数？各是多少？
def get_sum(num):
    result = []
    for i in range(1,num):
        for j in range(1,num):
            if( i != num ) and (i != j) and (j != num):
                result.append("%s%s%s"%(i,num,j))
    return result

print(get_sum(5))

# 判断xxx区间有多少个奇数和偶数
def su_num(start,end):
    odd_num = []
    even_num = []
    for i in range(start,end):
        if i %2!=0:
            odd_num.append(i)
        elif i!=0:
            even_num.append(i)
    return {"odd":odd_num,"even":even_num}

print(su_num(1,200))



# 判断俩json是否相等
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


# os模块
head,tail = os.path.split(os.path.dirname(__file__))
file_path ="InitEnviron.bat"
with open(file_path) as file:
    print(file.read())
    print(os.access(file_path, os.R_OK))
    print(os.access(file_path, os.X_OK))
    print(os.access(file_path, os.W_OK))

file.close()

# 删除字符串a中包含的字符串b，举例 输入a = "asdw",b = "sd" 返回 字符串 “aw”，并且测试这个程序
def delect_str(keyword,del_value):
    print(str(keyword).replace(del_value,""))
delect_str("asdw","sd")

# 把字符串转为数字，比如 str="1234"，变成 int 1234
def re_str_type(key):
    int_num = int(key)
    print(int_num,type(int_num))
re_str_type("11111")

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

# 给一个字符串，字符串里有 （）{}[]“”这六个符号，设计一个算法,判断这些符号是否成对匹配

# 去掉空格取出最后一组数
def count_str(word):
    split_str = word.split(" ")
    return len(split_str[-1])
print(count_str("hello nowcoder aaa bbb ccc b"))

# 字符类型分组
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

# 输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
def dis_tinct(num):
    change_str = str(num)[::-1]  # 反转后的字符串
    answer = []
    for i in change_str:
        if i not in answer:
            answer.append(i)
    return ("".join(answer))

print(dis_tinct(558996885221111992712833887211111565779552222))

# 生成N个1到1000之间的随机整数（N≤1000）
# 对于其中重复的数字，只保留一个
# 把其余相同的数去掉，不同的数对应着不同的学生的学号
# 然后再把这些数从小到大排序
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

# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
# 如果目标值不存在于数组中，返回它将会被按顺序插入的位置
# 你可以假设数组中无重复元素。

def find_index(lists,tangent):
    if type(lists) is not list:
        return False
    else:
        if tangent < lists[0]:
            return 0
        elif tangent >= lists[len(lists) - 1]:
            return len(lists)
        else:
            for i in range(len(lists)):
                if tangent == lists[i]:
                    return i
                elif tangent >lists[i] and tangent<=lists[i+1]:
                    return i+1
            # return lists.index(tangent)
print(find_index([1, 3, 5, 6], 5))