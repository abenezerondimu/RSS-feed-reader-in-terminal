import feedparser as fp

class Feed:
    parsed_data = None
    def __init__(self, rss_feed_url:str):
        #Validating input data
        rss_feed_url = rss_feed_url.casefold()
        url_size = len(rss_feed_url)
        if rss_feed_url[0:4] != "http":
            "f URL {rss_feed_url} is not valid!!"
        else:
            self.feed_url = rss_feed_url

    def feed(self):
        parsed_feed = fp.parse(self.feed_url)
        feed_length = len(parsed_feed.entries)
        count = 0
        news = ""
        while count < feed_length:
            news += parsed_feed.entries[count].title + "\n\n" + parsed_feed.entries[count].description + parsed_feed.entries[count].link + "\n\n"

            count += 1
        return news
    

rss_feed_url = input("Enter you RSS feed: ")
feed = Feed(rss_feed_url)
print(feed.feed())
