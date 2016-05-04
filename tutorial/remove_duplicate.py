from scrapy.dupefilters import RFPDupeFilter


class UrlFilter(RFPDupeFilter):

    def __init__(self, path=None, debug=False):
        self.urls_seen = set()
        RFPDupeFilter.__init__(self, path, debug)

    def request_seen(self, request):
        if request.url in self.urls_seen:
            print 'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP'
            print request.url
            print 'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP'
            return True
        else:
            self.urls_seen.add(request.url)
