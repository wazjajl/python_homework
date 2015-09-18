#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhangmingqian
# @Date:   2015-09-16 11:53:12
# @Last Modified by:   Administrator
# @Last Modified time: 2015-09-16 14:10:48

a = 1.1
b = 1.0 + 0.1
print id(a)
print id(b)

# ==.
if a == b:
    print "a = b."
else:
    print "a != b"

# is , not is.
if a is b:
    print "a is b."
else:
    print "but a is not b."
