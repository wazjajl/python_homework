#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhangmingqian
# @Date:   2015-09-16 10:52:16
# @Last Modified by:   Administrator
# @Last Modified time: 2015-09-17 15:10:10

# 方法（一）：
m = 6
n = m * 2 - 1
i = 1
# step one.
while i < m:
    j = 1
    while j < m - i:
        print " ",
        j += 1
    print "* " * (i * 2 - 1)
    i += 1

# step two.
o = 2
while i >= m and i < n - 1:
    j = 1
    while j < o:
        print " ",
        j += 1
    print "* " * ((m - o) * 2 - 1)
    o += 1
    i += 1

# -----------------------------------------
# 方法（二）：
# m = 6
# n = m * 2 - 1
# i = 1
# while i < m:
#     j = 1
# step one.
#     while j < m - i:
#         print " ",
#         j += 1
# step two.
#     while j >= m - i and j < m:
#         print "*",
#         j += 1
# step three.
#     while j >= m and j < n and j < m + i - 1:
#         print "*",
#         j += 1
# step four.
#     while j < n and j > m + i - 1:
#         print " ",
#         j += 1
#     i += 1
#     print

# o = 2
# while i >= m and i < n - 1:
#     j = 1
#     while j < o:
#         print " ",
#         j += 1
#     while j >= o and j < m:
#         print "*",
#         j += 1
#     while j < n - o:
#         print "*",
#         j += 1
#     while j > n - o and j < n:
#         print " ",
#         j += 1
#     o += 1
#     i += 1
#     print
