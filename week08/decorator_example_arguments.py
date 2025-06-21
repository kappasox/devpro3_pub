#!/usr/bin/env /usr/bin/python3
# -*- coding: utf-8 -*-

#
# Sample Implemantation of IPUT Course IoT Device Programming 3 (2023 Summer)
# Week 08
#
# Decorator example (w/ arguments)

# May 27, 2025
# Michiharu Takemoto (takemoto.development@gmail.com)

import sys

# 「引数が関数(f)」で「戻り値(new_func)も関数」の
# 関数(decorator_example)
def decorator_example(f):
    print(sys._getframe().f_code.co_name)
    print(f.__name__)
    def new_func(*args, **kwargs):
        print('Start!')
        ret_value = f(*args, **kwargs)
        print('End')
        return ret_value
 
    return new_func
 

def my_func1():
    print(sys._getframe().f_code.co_name)
    x = 10
    y = 20
    ret = x + y
    return ret

# @はコメントではない。
@decorator_example
def my_func2():
    print(sys._getframe().f_code.co_name)
    x = 10
    y = 20
    ret = x + y
    return ret

# この関数は使わないけど授業スライドには登場
def my_func3(x, y):
    print(sys._getframe().f_code.co_name)
    ret = x + y
    return ret

# my_func3()と同じだけど。
@decorator_example
def my_func4(x, y):
    print(sys._getframe().f_code.co_name)
    ret = x + y
    return ret

if __name__ == '__main__':
    print("Start if __name__ == '__main__'")

    print('--------')
    z = my_func1()
    print('my_func1', z)

    print('--------')
    z = my_func2()
    print('my_func2', z)
 
    print('--------')
    z = my_func3(10, 20)
    print('my_func3', z)

    print('--------')
    z = my_func4(10, 20)
    print('my_func4', z)