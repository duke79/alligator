import feedparser # https://pythonhosted.org/feedparser/reference.html


class Spider():
    def __init__(self):
        pass

    def get_sources(self):
        return [
            "http://www.wsj.com/xml/rss/3_7041.xml",
            # "http://www.wsj.com/xml/rss/3_7085.xml",
            # "http://www.wsj.com/xml/rss/3_7014.xml",
            # "http://www.wsj.com/xml/rss/3_7455.xml",
            # "http://www.wsj.com/xml/rss/3_7201.xml",
            # "http://www.wsj.com/xml/rss/3_7031.xml",
            "http://rss.cnn.com/rss/edition.rss"
        ]

    def parse_channel_by_url(self, url):
        data = feedparser.parse(url)
        return data

    def parse_all_channels(self):
        """
        This one is heavy.
        :return:
        """
        channels = list()
        for source in self.get_sources():
            channel = self.parse_channel_by_url(source)
            channels.append(channel)
        return channels

    def get_all_feed(self):
        """
        This one is heavy.
        :return:
        """
        feed = list()
        for source in self.get_sources():
            try:
                source_feed = self.parse_channel_by_url(source)
                for elem in source_feed:
                    feed.append(elem)
            except Exception as e:
                pass
        return feed
