import twitter
from my_info import *
import datetime


def changeDateFormat(str_dt):
    format = '%a %b %d %H:%M:%S %z %Y'
    dt_dt = datetime.datetime.strptime(str_dt,format)
    kst = dt_dt + datetime.timedelta(hours=9)
    format2 = '%Y.%m.%d  %p %I:%M'
    return datetime.datetime.strftime(kst, format2)


api = twitter.Api(consumer_key=twitter_consumer_key,
                  consumer_secret=twitter_consumer_secret,
                  access_token_key=twitter_access_token,
                  access_token_secret=twitter_access_token_secret)

account = "@BTS_twt"
result = api.GetUserTimeline(screen_name=account, count=200, include_rts=False, exclude_replies=True)
print(len(result))


for twt in result:
    print(changeDateFormat(twt.created_at))
    print(twt.text)
    if(twt.media):
        # print(twt.media[0])
        # print(twt.media[0].media_url_https)
        print(len(twt.media))
        pic_num = len(twt.media)
        for i in range(pic_num):
            print(twt.media[i].media_url_https)
    print()
    print()

print(result[7])
