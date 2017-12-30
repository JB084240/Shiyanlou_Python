# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from shiyanlougithub.models import Repository, engine
from shiyanlougithub.items import RepositoryItem
from datetime import datetime

#run command: scrapy crawl reposiotry

class ShiyanlougithubPipeline(object):
    def process_item(self, item, spider):
        origin_time = item['update_time'].split('T')
        item['update_time'] = datetime.strptime(origin_time[0] + ' ' + origin_time[1].strip('Z'), '%Y-%m-%d %H:%M:%S')
        self.session.add(Repository(**item))
        return item

    def open_spider(self, spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()


