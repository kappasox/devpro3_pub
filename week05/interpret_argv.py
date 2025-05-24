#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Sample Implemantation of IPUT Course IoT Device Programming 3 (2023 Summer)
# Week 05
#
# How to interpret argv (and argc)

# May 7, 2023
# Michiharu Takemoto (takemoto.development@gmail.com)

#
# NOT MIT License
#

import sys

DEFAULT_HOSTNAME = "www.iput.ac.jp"
DEFAULT_PORT = 2000

if __name__ == '__main__':
    print("Start if __name__ == '__main__'")

    sys_argc = len(sys.argv)
    count = 1

    print("sys_argc: " + str(sys_argc))
    print("sys.argv: " + str(sys.argv))

    hostname_v = DEFAULT_HOSTNAME
    port_v = DEFAULT_PORT

    while True:
        print(count, "/", sys_argc)
        if(count >= sys_argc):
            break

        option_key = sys.argv[count]
        print("option_key: "+ str(option_key))

        if ("-h" == option_key):
            count = count + 1
            hostname_v = sys.argv[count]
            print("hostname_v: " + hostname_v)

        if ("-p" == option_key):
            count = count + 1
            port_v = int(sys.argv[count])
            print("port_v: "+str(port_v))

        count = count + 1

    print("hostname_v: " + hostname_v)
    print("port_v: " + str(port_v))
    
