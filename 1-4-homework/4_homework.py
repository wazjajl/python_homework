#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2015-09-15 23:42:58
# @Last Modified by:   Administrator
# @Last Modified time: 2015-09-16 10:59:54

for i in xrange(1, 10):
    print str(i) + "|",
    for j in xrange(1, 10):
        print(i * j),
    print
