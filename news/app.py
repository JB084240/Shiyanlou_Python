#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, render_template, abort
import sys, os, json

app = Flask(__name__)
app.config['TEMPLATE_AUTO_RELOAD'] = True

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route('/')
def index():
    fdict_list = []
    file_list = os.listdir('/home/shiyanlou/files/')
    for file in file_list:
        file_path = '/home/shiyanlou/files/' + file
        print("file path is ", file_path)
        with open(file_path, 'r') as f:
            f_index = json.loads(f.read())
            fdict_list.append(f_index)
    return render_template('index.html', f_index=fdict_list)

@app.route('/files/<filename>')
def file_index(filename):
    filename_json = filename + '.json'
    file_path = '/home/shiyanlou/files/' + filename_json
    print("filename is ", file_path)
    if os.path.isfile(file_path):
        if filename == 'helloshiyanlou' or filename == 'helloworld':
            with open(file_path, 'r') as file:
                file_dict = json.loads(file.read())
   
                cont_list = file_dict['content'].split('\\n')
                file_dict['content'] = cont_list

                return render_template('file.html', file_dict=file_dict)

    abort(404)

if __name__ == '__main__':
    app.run()

