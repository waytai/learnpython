#########################################################################
#-*- coding:utf-8 -*-
# File Name: repeat.py
#########################################################################
#!/bin/python
def greater():
    print "hello"

def repeat(f, times):
    for i in range(times):
        f()

repeat(greater, 4)
