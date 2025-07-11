#!/usr/bin/env /usr/bin/python3
# -*- coding: utf-8 -*-

# Sample Implemantation of IPUT Course IoT Device Programming 3 (2023 Summer)
# Week 13
#
# fastener Example (02)b
# basic ... two Python codes

# July 2, 2023
# Michiharu Takemoto (takemoto.development@gmail.com)

# 
# MIT License
# 
# Copyright (c) 2023 Michiharu Takemoto <takemoto.development@gmail.com>
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
import time

import fasteners

LOCKFILE = './lock.txt'

def start_process1():
    func_name = sys._getframe().f_code.co_name
    count = 0

    lock = fasteners.InterProcessLock(LOCKFILE)

    with lock:
        while (count < 10):
            print(func_name + ": " + str(count))
            count = count + 1
            time.sleep(5)

def start_process2():
    func_name = sys._getframe().f_code.co_name
    count = 0

    lock = fasteners.InterProcessLock(LOCKFILE)

    with lock:
        while (count < 10):
            print(func_name + ": " + str(count))
            count = count + 1
            time.sleep(2)


if __name__ == "__main__":
    print("Start if __name__ == '__main__'")
    print()

    start_process2()
