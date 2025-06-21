#!/usr/bin/env /usr/bin/python3
# -*- coding: utf-8 -*-

# Sample Implemantation of IPUT Course IoT Device Programming 3 (2022 Summer)
# Week 06
#
# file read examples
#
# May 19, 2024
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


import sys
import csv

DATA_DIR = 'week06'
DATA_DIR = 'week06_file' 
CSV_FILENAME = 'csv_sample20220519.csv'
default_filename = DATA_DIR + '/' + CSV_FILENAME

def file_read_all_str(filename1 = default_filename):
    print(sys._getframe().f_code.co_name)
    with open(filename1, mode='r') as f:
        buff = f.read()
        print(buff)


def file_read7(filename1 = default_filename):
    print(sys._getframe().f_code.co_name)
    with open(filename1, mode='r') as f:
        buff = f.read(7)
        print(buff)


def file_read_one_line(filename1 = default_filename):
    print(sys._getframe().f_code.co_name)
    with open(filename1, mode='r') as f:
        buff = f.readline()
        print(buff)


def file_read_two_lines(filename1 = default_filename):
    print(sys._getframe().f_code.co_name)
    with open(filename1, mode='r') as f:
        buff = f.readline()
        print(buff)
        buff = f.readline()
        print(buff)


def file_read_two_lines_without_lf(filename1 = default_filename):
    print(sys._getframe().f_code.co_name)
    with open(filename1, mode='r') as f:
        buff = f.readline()
        buff1 = buff.replace('\n', '')
        print(buff1)
        buff = f.readline()
        buff1 = buff.replace('\n', '')
        print(buff1)


def file_read_all_list(filename1 = default_filename):
    print(sys._getframe().f_code.co_name)
    with open(filename1, mode='r') as f:
        buff = f.readlines()
        print(buff)


def simple_read_iterator(filename1 = default_filename):
    print(sys._getframe().f_code.co_name)
    with open(filename1, mode='r') as f:
        for row in f:
            print("I have got a row!", sys._getframe().f_code.co_name)
            print(row)


def csv_read_iterator(filename1 = default_filename):
    print(sys._getframe().f_code.co_name)
    with open(filename1, mode='r') as f:
        all_data_iter = csv.reader(f)
        for row in all_data_iter:
            print("I have got a row!", sys._getframe().f_code.co_name)
            print(row)

def csv_read_iterator_two_lists(filename1 = default_filename):
    print(sys._getframe().f_code.co_name)
    # Work A04 (IoT Device Programming 3 Week 6)
    #
    #
    return [10, 10], [100, 100]


def list_is_not_an_interator():
    print(sys._getframe().f_code.co_name)
    value_list = [1,2,3]
    print(value_list)
    first_value = value_list[0]
    print(first_value)
    first_value_by_next = next(value_list)
    print(first_value_by_next)


if __name__ == '__main__':
    print("Start if __name__ == '__main__'")
    print()

    file_v = CSV_FILENAME
    full_filename_v = DATA_DIR + '/' + CSV_FILENAME

    sys_argc = len(sys.argv)
    count = 1

    print(sys.argv)
    while True:
#        print(count, "/", sys_argc)
        if(count >= sys_argc):
            break

        option_key = sys.argv[count]
#        print(option_key)

        if ("-c" == option_key):
            count = count + 1
            file_v = sys.argv[count]
            print(option_key, file_v)
            full_filename_v = DATA_DIR + '/' + file_v

        if ("-f" == option_key):
            count = count + 1
            full_filename_v = sys.argv[count]
            print(option_key, full_filename_v)

        if ("-h" == option_key):
            #count = count + 1
            print('help for ', sys.argv[0])
            print('  -c csv filename (in data directory)')
            print('  -f csv filename (full path)')
            sys.exit()

        count = count + 1

    #print(full_filename_v)

    file_read7(full_filename_v)
    print()
    file_read_all_str(full_filename_v)
    print()
    file_read_all_list(full_filename_v)
    print()
    file_read_one_line(full_filename_v)
    print()
    file_read_two_lines(full_filename_v)
    print()
    file_read_two_lines_without_lf(full_filename_v)

    print() 
    csv_read_iterator(full_filename_v)
    print()
    simple_read_iterator(full_filename_v)
    print()

    print()
    t, h = csv_read_iterator_two_lists(full_filename_v)
    print('Temp -- '+ str(t))
    print('Humid --- ' + str(h))

    print('-----')
    print('Error will be occurred intentionally by Takemoto!')
    list_is_not_an_interator()

