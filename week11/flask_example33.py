#!/usr/bin/env /usr/bin/python3
# -*- coding: utf-8 -*-

# Sample Implemantation of IPUT Course IoT Device Programming 3 (2023 Summer)
# Week 11
#
# Flask Example (33)
# render_template with Python data (list of list)
# JavaScript example (get_average)

# June 23, 2023
# Michiharu Takemoto (takemoto.development@gmail.com)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index1():
    print("Hello! (to Terminal)")

    data_list = []
    data_list.append([35.2, 43.0])
    data_list.append([27.5, 32.0])
    data_list.append([24.0, 36.0])
    data_list.append([18.0, 5.0])
    return render_template("flask_example33_tmp.html",  input_from_python = data_list) 

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5001, debug=True)
