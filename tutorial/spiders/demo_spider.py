import urlparse

import scrapy as scrapy

from tutorial.items import TutorialItem


class DemoSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["qiushibaike.com"]

    start_urls = [
        "http://www.qiushibaike.com/"
    ]

    def parse(self, response):

        # title = response.xpath('/html/head/title/text()').extract()
        for content in response.xpath('//*[@class="article block untagged mb15"]/div[2]/text()').extract():
            print 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
            item = TutorialItem()
            item['title'] = content
            yield item

        for url in response.xpath('//*[@id="content-left"]/ul[@class="pagination"]/li/a/@href'):
            if url:
                new_url = urlparse.urljoin(response.url, url.extract())
                yield scrapy.Request(url=new_url, callback=self.parse)