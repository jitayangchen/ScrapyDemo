import urlparse

import scrapy as scrapy

from tutorial.items import TutorialItem


class DemoSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["findfine.com.cn"]

    start_urls = [
        "http://www.findfine.com.cn/"
    ]

    count = 1

    def parse(self, response):

        title = response.xpath('/html/head/title/text()').extract()
        item = TutorialItem()
        item['title'] = title
        yield item

        for url in response.xpath('//a/@href').extract():
            new_url = urlparse.urljoin(response.url, url)
            yield scrapy.Request(url=new_url, callback=self.parse)