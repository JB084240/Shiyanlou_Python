# -*- coding:utf-8 -*-

#pre-condition: install scrapy: sudo pip3 install sctapy
#command: scrapy runspider filename.py -o outputfilename.json


import scrapy

class Shiyanlou_Git(scrapy.Spider):

    name = 'shiyanlou_git'

    @property
    def start_urls(self):

        url_templ = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_templ.format(i) for i in range(1,4))


    def parse(self, response):
        for course in response.css('li.col-12'):
            yield{
                "name": course.css('div.d-inline-block a::text').re_first('(\w.+\w$)[\W]*'),
                #"name": course.css('div.d-inline-block a::text').re_first('[\n\s*(.*)'),
                
                "update_time": course.css('div.text-gray relative-time::attr(datetime)').re_first('[^\d]*(\d*.+Z$)[.]*')

                #"update_time": course.css('.//div[contains(@class,"f6"]/relative-time').re('[^\d]*(\d*.+Z$).*'),
            }


