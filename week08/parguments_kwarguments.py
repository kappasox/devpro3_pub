#!/usr/bin/env /usr/bin/python3
# -*- coding: utf-8 -*-

# Sample Implemantation of IPUT Course IoT Device Programming 3 (2022 Summer)
# Week 08
#
# (Positonal) Arugments and
# Keyword Arugements
#
# May 26, 2025
# Michiharu Takemoto (takemoto.development@gmail.com)
#
#
# MIT License
# 
# Copyright (c) 2025 Michiharu Takemoto <takemoto.development@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 
# 

import sys

def func1(x, y):
    print(sys._getframe().f_code.co_name)
    print(type(x), str(x))
    print(type(y), str(y))


def func2(x=100, y=100):
    print(sys._getframe().f_code.co_name)
    print(type(x), str(x))
    print(type(y), str(y))


def func3(*args):
    print(sys._getframe().f_code.co_name)
    print(type(args), str(args))
    
    for a in args:
        print(type(a), str(a))


def func4(*positional_args):
    print(sys._getframe().f_code.co_name)
    print(type(positional_args), str(positional_args))
    
    for a in positional_args:
        print(type(a), str(a))


def func5(**kwargs):
    print(sys._getframe().f_code.co_name)
    print(type(kwargs), str(kwargs))
    
    for a in kwargs:
        print(type(a), str(a))

    x0 = kwargs.get('x')
    print('x =', str(x0))

    y0 = kwargs.get('y')
    print('y =', str(y0))


def func6(*args, **kwargs):
    print(sys._getframe().f_code.co_name)
    print(type(args), str(args))
    print(type(kwargs), str(kwargs))


if __name__ == '__main__':
    print("Start if __name__ == '__main__'")
  
    print('---------')
    func1(1,2)
  #  print('---------')
  #  func1(3)
    print('---------')
    print('---------')
    func2(1,2)
    print('---------')
    func2(3)
    print('---------')
    print('---------')
    func3(1)
    print('---------')
    func3(1, 2)  
    print('---------')
    print('---------')
    func4(1, 2)  
    print('---------')
    print('---------')
    func5(x=1, y=2)  
    print('---------')
    func5(y=2, x=1)  
    print('---------')
    func5(x=1)  
    print('---------')
    func5(y=2, z=10)  
    print('---------')
    print('---------')
    func6(x=1)  
    print('---------')
    func6(2) 
    print('---------')
    func6()  