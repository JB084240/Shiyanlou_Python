# -*- coding:utf-8 -*-

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
                "name": course.css('div.d-inline-block a::text()').extract_first(),
                #"name": course.css('.//div[contains(@class,"d-inline-block")]/a/text()[2]').extract_first(),
                
                #"update_time": course.css('div.f6 relative-time').re('[^\d]*(\d*.+Z$).*'),

                "update_time": course.css('.//div[contains(@class,"f6"]/relative-time').re('[^\d]*(\d*.+Z$).*'),
            }


