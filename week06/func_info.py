#!/usr/bin/env /usr/bin/python3
# -*- coding: utf-8 -*-

# Sample Implemantation of IPUT Course IoT Device Programming 3 (2022 Summer)
#
# Week 06
# How to use sys._getframe().f_code.co_name and __name__, __doc__, and dir().

#
# May 22, 2024
# Michiharu Takemoto (takemoto.development@gmail.com)
#
#
# MIT License
# 
# Copyright (c) 2024 Michiharu Takemoto <takemoto.development@gmail.com>
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

def function_test1():
    import sys
    print(sys._getframe().f_code.co_name)

def function_test2():
    """
    2024/05/22 
    ここに関数のコメントを書ける。日本語OK。
    """
    print('Hello, function_test2!')
    x = 10
    print('x =', x)

if __name__ == '__main__':
    print("Start if __name__ == '__main__'")
    print()

    print('---------------------')
    print('How to use sys._getframe().f_code.co_name')
    function_test1()

    print('---------------------')
    print('How to use .__name__ , .__doc__ , and dir() for a function.')

    print(function_test2.__name__)

    print('--------')
    print('function_test2.__name__')
    print(function_test2.__name__)
    print('----')
    print('function_test2.__doc__')
    print(function_test2.__doc__)
    print('----')
    print('dir(function_test2)')
    print(dir(function_test2))