from scrapy.dupefilters import RFPDupeFilter


class url_filter(RFPDupeFilter):

    def request_seen(self, request):
        print 'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP'
        print request.url
        print 'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP'