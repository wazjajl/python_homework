#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhangmingqian
# @Date:   2015-09-16 15:26:19
# @Last Modified by:   Administrator
# @Last Modified time: 2015-09-17 16:17:43

# total = 7
# key_total = total * 2 - 1
# i = 1
# while i < total:
#     j = 1
#     while j < total - i:
#         print " ",
#         j += 1
#     while j > total - i - 1 and j < total:
#         print total - j,
#         j += 1
#     while j >= total and j < total * 2 - - 2:
#         print j - total + 2,
#         j += 1
#     i += 1
#     print

# m = 8
# n = m * 2 - 1
# i = 1
# while i < m:
#     j = 1
#     while j < m:
#         if j >= m - i:
#             print m - j,
#         else:
#             print " ",
#         j += 1
#     while j >= m and j < n:
#         if j < m + i - 1:
#             print j - m + 2,
#         else:
#             print " ",
#         j += 1
#     i += 1
#     print


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
# while i >= m and i < n:
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

# m = 6
# n = m * 2 - 1
# i = 1
# while i < m:
#     j = 1
#     while j < m - i:
#         print " ",
#         j += 1
#     print "* " * (i * 2 - 1)
#     i += 1

# o = 2
# while i >= m and i < n - 1:
#     j = 1
#     while j < o:
#         print " ",
#         j += 1
#     print "* " * ((m - o) * 2 - 1)
#     o += 1
#     i += 1


i = 0
while i < 7:
    j = 1
    space = " " * 2 * (6 - i)
    print space,
    while j <= i:
        print "*",
        j += 1
    r = 1
    while r < i:
        print "*",
        r += 1
    print
    i += 1
