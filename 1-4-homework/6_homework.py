#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhangmingqian
# @Date:   2015-09-16 10:06:58
# @Last Modified by:   Administrator
# @Last Modified time: 2015-09-17 18:52:32

# 方法（一）：
input_num = int(raw_input("Please input a integer number whitin 15: "))
# jugement the number.
while input_num not in xrange(1, 16):
    print "Input is not correct or not in range."
    input_num = int(raw_input("Please input a integer number whitin 15: "))
# output the number.
m = input_num + 1
n = m * 2 - 1
i = 1
while i < m:
    j = 1
    space = " " * 2 * (m - i - 1)
    # step one.
    print space,
    while j <= i:
        print i - j + 1,
        j += 1
    # step two.
    o = 1
    while o < i:
        print o + 1,
        o += 1
    # step three.
    i += 1
    print


# 方法（二）：
#input_num = int(raw_input("Please input a integer number whitin 15: "))
# input_num = 8
# jugement the number.
# while input_num not in xrange(1, 16):
#     print "Input is not correct or not in range."
#     input_num = int(raw_input("Please input a integer number whitin 15: "))
# output the number.
# m = input_num + 1
# n = m * 2 - 1
# i = 1
# while i < m:
#     j = 1
# step one.
#     while j < m:
#         if j >= m - i:
#             print m - j,
#         else:
#             print " ",
#         j += 1
# step two.
#     while j >= m and j < n:
#         if j < m + i - 1:
#             print j - m + 2,
#         else:
#             print " ",
#         j += 1
# step three.
#     i += 1
#     print
