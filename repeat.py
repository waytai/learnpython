#########################################################################
#-*- coding:utf-8 -*-
# File Name: repeat.py
#########################################################################
#!/bin/python
def greeter():
    print "hello"

def repeat(f, times):
    for i in range(times):
        f()

repeat(greeter, 4)

print "-"*30

def print_call(fn):
    def fn_wrap(*args, **kwargs): #take any arguments
        print "Calling %s" % (fn.func_name)
        return fn(*args, **kwargs) #pass any arguments to fn()
    return fn_wrap


greeter = print_call(greeter) #wrap greeter
repeat(greeter, 3)
