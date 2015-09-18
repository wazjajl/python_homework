#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2015-09-15 23:48:06
# @Last Modified by:   Administrator
# @Last Modified time: 2015-09-17 13:47:10

# template one.
print "Template-01:"
i = 1
while i < 7:
    i += 1
    j = 1
    while j < i:
        print j,
        j += 1
    print

# template two.
print "---------------"
print "Template-02:"
i = -6
while i < 0:
    j = 1
    while j <= -i:
        print j,
        j += 1
    print
    i += 1

# template three
#(第一种方法).
print "---------------"
print "Template-03:"
total = 7
i = 1
while i < total:
    j = 1
    while j < total - i:
        print " ",
        j += 1
    while j > total - i - 1 and j < total:
        print total - j,
        j += 1
    i += 1
    print

#(第二种方法).
total = 7
i = 1
while i < total:
    j = 1
    while j < total:
        if j >= total - i:
            print total - j,
        else:
            print " ",
        j += 1
    i += 1
    print
