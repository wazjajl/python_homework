#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhangmingqian
# @Date:   2015-09-16 11:09:52
# @Last Modified by:   Administrator
# @Last Modified time: 2015-09-16 11:30:02

key_num = ""
for i in xrange(1, 10):
    key_num += str(i)
    key_sum = int(key_num) * 8 + i
    print key_num, " * ", str(8), " + ", str(i), " = ", str(key_sum)
