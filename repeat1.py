#########################################################################
#-*- coding:utf-8 -*-
# File Name: repeat1.py
#########################################################################
#!/bin/python
def print_call(fn):
    def fn_wrap(*args, **kwargs):
       print "*"*30
       print "Calling %s with arguments: \n\targs: %s\n\tkwargs:%s" %(fn.__name__, args, kwargs)
       retval = fn(*args, **kwargs)
       print "%s returning '%s'" % (fn.func_name, retval)
       return retval
    print "%"*30
    print fn.func_name
    print fn_wrap.func_name
    fn_wrap.func_name = fn.func_name
    print "i"*30
    return fn_wrap

def greeter(greeting, what='world'):
    return "%s %s!" % (greeting, what)
greeter = print_call(greeter)
greeter("Hi")

#greeter("Hi", what="Python")
