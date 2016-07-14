#########################################################################
#-*- coding:utf-8 -*-
# File Name: comprehension.py
#########################################################################
#!/bin/python
num = [1, 4, -5, 10, -7, 2, 3, -1]
print filter(lambda x:x>0, num)
filter_and_squared = map(lambda x:x**2, filter(lambda x:x>0, num))
print filter_and_squared
