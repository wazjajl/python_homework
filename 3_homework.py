#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhangmingqian
# @Date:   2015-09-15 18:02:52
# @Last Modified by:   Administrator
# @Last Modified time: 2015-09-15 18:09:40

rownum = int(raw_input("Please input the number of rows: "))
i = 1
# control the output rows.
while i <= rownum:
    i += 1
    j = 1
    nsum = 0
    nlist = []
    # append the number to a list.
    while j < i:
        nsum += j
        nlist.append(str(j))
        j += 1
    # output the result.
    print '+'.join(nlist),
    print "= " + str(nsum)
