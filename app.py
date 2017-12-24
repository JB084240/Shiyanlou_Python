#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, render_template, abort
import sys, os, json

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['TEMPLATE_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/news'
db = SQLAlchemy(app)

##added for chanllenge database##

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',backref=db.backref('file', lazy = 'dynamic'))
    content = db.Column(db.Text)
    
    def __init__(self, title, category, content):
        self.title = title
        self.created_time = datetime.utcnow()
        self.category = category
        self.content = content
    
    def __repr__(self):
        return '<File %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name

###end 

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.route('/files/<file_Id>')
def file(file_Id):
    from sqlalchemy import create_engine
    engine = create_engine('mysql://root:@localhost/news')
    file_list = engine.execute('select * from file').fetchall()
    for file_tup in file_list:
        if file_Id == file_tup[0]:
            return render_template('file_id.html', file_tup=file_tup)
    
    abort(404)


@app.route('/')
def index():
    file_list = os.listdir('/home/shiyanlou/files/')
    fdict_list = []
    for file in file_list:
        file_path = '/home/shiyanlou/files/' + file
        with open(file_path, 'r') as f:
            f_index = json.loads(f.read())
            filename = file.split('.')
            path = '/files/' + filename[0]
            f_index['path'] = path
            fdict_list.append(f_index)
    return render_template('index.html', f_index=fdict_list)


@app.route('/files/<filename>')
def file_index(filename):
    filename_json = filename + '.json'
    file_path = '/home/shiyanlou/files/' + filename_json
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

