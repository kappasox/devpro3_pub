#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Sample Implemantation of IPUT Course IoT Device Programming 3 (2023 Summer)
# Week 05
#
# CSV file write/read example

# May 19, 2024
# Michiharu Takemoto (takemoto.development@gmail.com)

#
# NOT MIT License
#

import sys
import csv

DATA_DIR = 'week05/data'
CSV_FILENAME = 'csv_sample.csv'
filename = DATA_DIR + '/' + CSV_FILENAME

def function_test():
    """
    function_test()
    2022/05/19
    (ここに関数のコメントを書ける。日本語OK。)
    (week05の授業では配布するが、説明しない。
    質問があれば、説明する。)
    """
    print(function_test.__name__)
    print(function_test.__doc__)
    print(dir(function_test))

def csv_write_one_file(data_str):
    with open(filename, mode='a') as f:
        f.write(data_str)
        f.write('\n')


def csv_write_without_iterator(data_list_list):
    with open(filename, mode='a') as f:
        for row in data_list_list:
            data1 = row[0]
            data2 = row[1]
            row_str = str(data1) + ',' + str(data2)
            f.write(row_str)
            f.write('\n')


def csv_write_iterator(data_list_list):
    with open(filename, mode='a') as f:
        write_iter = csv.writer(f)
        for row in data_list_list:
            write_iter.writerow(row)



def csv_read_one_file():
    with open(filename) as f:
        all_data = f.read()
        print(all_data)
    # f = open(filename)
    # all_data = f.read()
    # print(all_data)
    # f.close()

def csv_read_iterator():
    with open(filename) as f:
        all_data_iter = csv.reader(f)
        for row in all_data_iter:
            print(row)
    

if __name__ == '__main__':
    print("Start if __name__ == '__main__'")

    sys_argc = len(sys.argv)
    count = 1
    d1_v = '123.4'
    d2_v = '56.7'

    while True:
        print(count, "/", sys_argc)
        if(count >= sys_argc):
            break

        option_key = sys.argv[count]
        print(option_key)

        if ("-d1" == option_key):
            count = count + 1
            d1_v = sys.argv[count]
            print(option_key, d1_v)

        if ("-d2" == option_key):
            count = count + 1
            d2_v = sys.argv[count]
            print(option_key, d2_v)

        count = count + 1
    
    #data_str_v = '123.4, 56.7'
    data_str_v = d1_v + ',' + d2_v
    csv_write_one_file(data_str_v) 

    data_list_list_v2 = [ [77.77, 77.77], [88.88, 88.88]]
    csv_write_without_iterator(data_list_list_v2)

    data_list_list_v = [ [11.11, 22.22], [33.33, 44.44], [55.55, 66.66]]
    csv_write_iterator(data_list_list_v)


    csv_read_one_file() 

    csv_read_iterator()

    #function_test()
