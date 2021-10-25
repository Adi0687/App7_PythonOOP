import yagmail
import pandas
from news import NewsFeed
import datetime
import time


def send_bulk_emails():
    global news
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    news = NewsFeed(interest=row['interest'],
                    from_date=yesterday,
                    to_date=today,
                    language='en')
    email = yagmail.SMTP(user="", password="")
    email.send(to=row['email'],
               subject=f"Your {row['interest']} news for today",
               contents=f"Hi{row['name']}\n See what's on about {row['interest']} today! \n {news.get()}\nAadil")


while True:
    if datetime.datetime.hour == 6 and datetime.datetime.minute == 0:

        df = pandas.read_excel("people.xlsx")

        for index, row, in df.iterrows():
            send_bulk_emails()
    time.sleep(60)
