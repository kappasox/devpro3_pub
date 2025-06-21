#!/usr/bin/env /usr/bin/python3
# -*- coding: utf-8 -*-

# Sample Implemantation of IPUT Course IoT Device Programming 3 (2023 Summer)
# Week 07
#
# Flask Example (14)
# render_template with Python data (list)

# May 27, 2023
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

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index1():
    print("Hello! (to Terminal)")
    data_list = [10, 20, 30, 40]
    for value in data_list:
        print(value)
    return render_template("flask_example14_tmp.html",  input_from_python = data_list) 

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5001, debug=True)


