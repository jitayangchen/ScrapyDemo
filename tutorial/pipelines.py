# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TutorialPipeline(object):
    file = open('output.txt', 'w')

    def process_item(self, item, spider):
        print 'XXXXXXXXXXXXX'
        print item['title'].encode('utf-8')
        print 'XXXXXXXXXXXXX'
        self.save_file(item['title'].encode('utf-8'))
        return item

    def save_file(self, title):

        self.file.write(title)
        self.file.write('\n')