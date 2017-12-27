#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#pre-condition env:
#sudo pip3 install mysqlclient
#sudo pip3 install Flask_SQLAlchemy

#activate the mysql and mongodb by:
#sudo service mysql start
#mysql -u root
#create database news;
#use news;
#sudo service mongod start


from flask import Flask, render_template, abort
import sys, os, json

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
mon = client.filetag

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
    category = db.relationship('Category',backref=db.backref('file'))
    content = db.Column(db.Text)
    
    def __init__(self, title, category, content):
        self.title = title
        self.created_time = datetime.utcnow()
        self.category = category
        self.content = content

    def __repr__(self):
        return '<File %r>' % self.title

    def add_tag(self, tag_name):
        for tag_list in mon.user.find():
            if tag_list['id'] == self.id and tag_name == tag_list['tag']:
                break
        tag = {'id': self.id, 'tag': tag_name}
        mon.user.insert_one(tag)

    def remove_tag(self, tag_name):
        for tag_list in mon.user.find():
            if tag_list['id'] == self.id and tag_list['tag'] == tag_name:
                mon.user.delete_one(tag_list)

    @property
    def tags(self):
        id_tag = []
        for tag_list in mon.user.find():
            if tag_list['id'] == self.id:
                id_tag.append(tag_list['tag'])
        return id_tag


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
    file_dict = File.query.filter_by(id=file_Id).first()
    if file_dict:
        return render_template('file.html', file_dict=file_dict)
    
    abort(404)


@app.route('/')
def index():
    f_index = db.session.query(File).all()
    if f_index:
        return render_template('index.html', f_index=f_index)


'''

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

'''

if __name__ == '__main__':
    app.run()

