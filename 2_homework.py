#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhangmingqian
# @Date:   2015-09-15 18:12:26
# @Last Modified by:   Administrator
# @Last Modified time: 2015-09-15 18:27:47

print "能被17整除的是："
j = 1
# output the number divided by 17.
for i in xrange(100, 1000):
    if i % 17 == 0:
        print i,
        i += 1
        j += 1
        # output ten numbers every row.
        if j % 11 == 0:
            print
            j = 1
