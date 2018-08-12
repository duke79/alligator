import feedparser # https://pythonhosted.org/feedparser/reference.html


class Spider():
    def __init__(self):
        pass

    def get_sources(self):
        # Sources from - https://guides.nyu.edu/c.php?g=276615&p=1845079
        source = [
            #WallStreetJournal
            "http://www.wsj.com/xml/rss/3_7041.xml",
            "http://www.wsj.com/xml/rss/3_7085.xml",
            "http://www.wsj.com/xml/rss/3_7014.xml",
            "http://www.wsj.com/xml/rss/3_7455.xml",
            "http://www.wsj.com/xml/rss/3_7201.xml",
            "http://www.wsj.com/xml/rss/3_7031.xml",
            #BBC - http://news.bbc.co.uk/2/hi/help/3223484.stm
            "http://feeds.bbci.co.uk/news/rss.xml",
            "http://feeds.bbci.co.uk/news/rss.xml?edition=int",
            "http://feeds.bbci.co.uk/news/world/rss.xml",
            "http://feeds.bbci.co.uk/news/uk/rss.xml",
            "http://feeds.bbci.co.uk/news/business/rss.xml",
            "http://feeds.bbci.co.uk/news/politics/rss.xml",
            "http://feeds.bbci.co.uk/news/health/rss.xml",
            "http://feeds.bbci.co.uk/news/education/rss.xml",
            "http://feeds.bbci.co.uk/news/science_and_environment/rss.xml",
            "http://feeds.bbci.co.uk/news/technology/rss.xml",
            "http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml",
            "http://feeds.bbci.co.uk/news/world/africa/rss.xml",
            "http://feeds.bbci.co.uk/news/world/asia/rss.xml",
            "http://feeds.bbci.co.uk/news/world/europe/rss.xml",
            "http://feeds.bbci.co.uk/news/world/latin_america/rss.xml",
            "http://feeds.bbci.co.uk/news/world/middle_east/rss.xml",
            "http://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml",
            "http://feeds.bbci.co.uk/news/england/rss.xml",
            "http://feeds.bbci.co.uk/news/northern_ireland/rss.xml",
            "http://feeds.bbci.co.uk/news/scotland/rss.xml",
            "http://feeds.bbci.co.uk/news/wales/rss.xml",
            "http://feeds.bbci.co.uk/news/magazine/rss.xml",
            "http://feeds.bbci.co.uk/news/also_in_the_news/rss.xml",
            "http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/in_pictures/rss.xml",
            "http://feeds.bbci.co.uk/news/special_reports/rss.xml",
            "http://feeds.bbci.co.uk/news/have_your_say/rss.xml",
            "https://www.bbc.co.uk/blogs/theeditors/rss.xml",
            #TheNewYorkTimes - more @ https://archive.nytimes.com/www.nytimes.com/services/xml/rss/index.html
            "https://www.nytimes.com/services/xml/rss/nyt/HomePage.xml",
            "http://rss.nytimes.com/services/xml/rss/nyt/World.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/Africa.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/Americas.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/AsiaPacific.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/Europe.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/MiddleEast.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/US.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/Education.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/Politics.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/NYRegion.xml",
            "http://cityroom.blogs.nytimes.com/feed/",
            "http://fort-greene.blogs.nytimes.com/feed",
            "http://eastvillage.thelocal.nytimes.com/feed/",
            "http://feeds.nytimes.com/nyt/rss/Business",
            "https://www.nytimes.com/services/xml/rss/nyt/EnergyEnvironment.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/SmallBusiness.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/Economy.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/Dealbook.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/MediaandAdvertising.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/YourMoney.xml",
            "http://feeds.nytimes.com/nyt/rss/Technology",
            "http://bits.blogs.nytimes.com/feed/",
            "https://www.nytimes.com/services/xml/rss/nyt/PersonalTech.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/Sports.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/Baseball.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/CollegeBasketball.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/CollegeFootball.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/Golf.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/Hockey.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/ProBasketball.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/ProFootball.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/Soccer.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/Tennis.xml",
            "http://gambit.blogs.nytimes.com/feed/",
            "https://www.nytimes.com/services/xml/rss/nyt/Science.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/Environment.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/Space.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/Health.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/Research.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/Nutrition.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/HealthCarePolicy.xml",
            "https://www.nytimes.com/services/xml/rss/nyt/Views.xml"
        ]

        return list(set(source))

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
