#!/usr/bin/env /usr/bin/python3
# -*- coding: utf-8 -*-

#
# Sample Implemantation of IPUT Course IoT Device Programming 3 (2023 Summer)
# Week 07
#
# Decorator example

# May 27, 2023
# Michiharu Takemoto (takemoto.development@gmail.com)

import sys

# 「引数が関数(f)」で「戻り値(new_func)も関数」の
# 関数(decorator_example)
def decorator_example(f):
    print(sys._getframe().f_code.co_name)
    def new_func():
        print('Start!')
        ret_value = f()
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

if __name__ == '__main__':
    print("Start if __name__ == '__main__'")
    print()

    z = my_func1()
    print('my_func1', z)
    print()

    z = my_func2()
    print('my_func2', z)
 