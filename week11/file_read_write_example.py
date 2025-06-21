#!/usr/bin/env /usr/bin/python3
# -*- coding: utf-8 -*-

# Sample Implemantation of IPUT Course IoT Device Programming 3 (2024 Summer)
# Week 11
#
# file read and write examples

# July 03, 2024
# Michiharu Takemoto (takemoto.development@gmail.com)

#
# NOT MIT License
#

import sys
import csv

#DATA_DIR = 'data'
DATA_DIR = 'week11/data'

CSV_FILENAME = 'csv_sample230515.csv'
default_filename = DATA_DIR + '/' + CSV_FILENAME
CSV_FILENAME_W = 'csv_sample230515_w.csv'
default_filename_w = DATA_DIR + '/' + CSV_FILENAME_W

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
            print("I have got a row!")
            print(row)


def csv_read_iterator(filename1 = default_filename):
    print(sys._getframe().f_code.co_name)
    with open(filename1, mode='r') as f:
        all_data_iter = csv.reader(f)
        for row in all_data_iter:
            print("I have got a row!")
            print(row)


def csv_read_list(filename1 = default_filename):
    print(sys._getframe().f_code.co_name)
    ret_list = []      # added (2022/06/26)
    with open(filename1, mode='r') as f:
        all_data_iter = csv.reader(f)
        for row in all_data_iter:
            #print("I have got a row!") # commented-out (2022/06/27)
            #print(row) # commented-out (2022/06/27)
            ret_list.append(row) # added (2022/06/26)

    return ret_list # added (2022/06/26)


def csv_write_list(filename1 = default_filename_w, data_list1=[[123.0, 100.0], [10.1, 12.2]]):
    print(sys._getframe().f_code.co_name)
    print(filename1)
    with open(filename1, mode='w', newline='') as f:
        writer = csv.writer(f)
        for row in data_list1:
            writer.writerow(row) 


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
    full_filename_w_v = DATA_DIR + '/' + CSV_FILENAME_W

    sys_argc = len(sys.argv)
    count = 1

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

        if ("-w" == option_key):
            count = count + 1
            full_filename_w_v = sys.argv[count]
            print(option_key, full_filename_w_v)

        if ("-h" == option_key):
            #count = count + 1
            print('help for ', sys.argv[0])
            print('  -c csv filename (in data directory)')
            print('  -f csv filename (full path)')
            print('  -w output csv filename (full path)')
            sys.exit()

        count = count + 1

    #print(full_filename_v)

    # file_read7(full_filename_v)
    # print()
    # file_read_all_str(full_filename_v)
    # print()
    # file_read_all_list(full_filename_v)
    # print()
    # file_read_one_line(full_filename_v)
    # print()
    # file_read_two_lines(full_filename_v)
    # print()
    # file_read_two_lines_without_lf(full_filename_v)
    # print()
    # csv_read_iterator(full_filename_v)


    data_list = csv_read_list(full_filename_v)
    print(data_list)

    csv_write_list(full_filename_w_v, [[20, 30], [21, 32], [111,112]])

    # print()
    # simple_read_iterator(full_filename_v)

    # print()
    # list_is_not_an_interator()

