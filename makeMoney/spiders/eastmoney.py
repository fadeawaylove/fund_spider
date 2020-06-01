# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'eastmoney'
    allowed_domains = ['fund.eastmoney.com/']
    start_urls = ['http://fund.eastmoney.com/data/fundranking.html']


    def start_requests(self):
        yield 
        
        pass

    def parse(self, response):
        print(response)
