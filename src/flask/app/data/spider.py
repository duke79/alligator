import feedparser  # https://pythonhosted.org/feedparser/introduction.html


class Spider():
    def __init__(self):
        pass

    def get_sources(self):
        return [
            {
                "title": "Opinion",
                "site": "wsj.com",
                "url": "http://www.wsj.com/xml/rss/3_7041.xml",
                "found_at": "http://www.wsj.com/public/page/rss_news_and_feeds.html"
            },
            {
                "title": "World News",
                "site": "wsj.com",
                "url": "http://www.wsj.com/xml/rss/3_7085.xml",
                "found_at": "http://www.wsj.com/public/page/rss_news_and_feeds.html"
            },
            {
                "title": "U.S. Business",
                "site": "wsj.com",
                "url": "http://www.wsj.com/xml/rss/3_7014.xml",
                "found_at": "http://www.wsj.com/public/page/rss_news_and_feeds.html"
            },
            {
                "title": "Technology: What's News",
                "site": "wsj.com",
                "url": "http://www.wsj.com/xml/rss/3_7455.xml",
                "found_at": "http://www.wsj.com/public/page/rss_news_and_feeds.html"
            },
            {
                "title": "Lifestyle",
                "site": "wsj.com",
                "url": "http://www.wsj.com/xml/rss/3_7201.xml",
                "found_at": "http://www.wsj.com/public/page/rss_news_and_feeds.html"
            },
            {
                "title": "Markets News",
                "site": "wsj.com",
                "url": "http://www.wsj.com/xml/rss/3_7031.xml",
                "found_at": "http://www.wsj.com/public/page/rss_news_and_feeds.html"
            }
        ]

    def parse_feed(self, url):
        data = feedparser.parse(url)
        entries = data["entries"]
        return entries

    def get_all_feed(self):
        """
        This one is heavy.
        :return:
        """
        feed = list()
        for source in spider.get_sources():
            try:
                source_feed = spider.parse_feed(source["url"])
                for elem in source_feed:
                    feed.append(elem)
            except Exception as e:
                pass
        return feed


spider = Spider()
feed = spider.get_all_feed()

print(feed)