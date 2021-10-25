# b79f1ba33a0d476b96bac4644251bb16
import requests


class NewsFeed:
    """Get a newsfeed based on passed parameters"""

    # class variable, always the same
    base_url = "https://newsapi.org/v2/everything?"
    api_key = "b79f1ba33a0d476b96bac4644251bb16"

    def __init__(self, interest, from_date, to_date, language="en"):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self._build_url()
        articles = self._get_article(url)

        email_body = ''
        for article in articles:
            email_body += article['title'] + "\n" + article['url'] + "\n\n"

        return email_body

    def _get_article(self, url):
        r = requests.get(url)
        content = r.json()
        articles = content['articles']
        return articles

    def _build_url(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}&" \
              f"apiKey={self.api_key}"
        return url


if __name__ == "--main__":
    news_feed = NewsFeed(interest='Tesla', from_date='2021-9-25', to_date='2021-10-24', language='en')
    print(news_feed.get())
