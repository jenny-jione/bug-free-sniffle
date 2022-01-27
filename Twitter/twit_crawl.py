import twitter
from my_info import *
import datetime
import csv


def changeDateFormat(str_dt):
    format = '%a %b %d %H:%M:%S %z %Y'
    dt_dt = datetime.datetime.strptime(str_dt,format)
    kst = dt_dt + datetime.timedelta(hours=9)
    format2 = '%Y.%m.%d  %p %I:%M'
    return datetime.datetime.strftime(kst, format2)


def save_to_file(twts):
    print("save to file")
    file = open(my_path + f"/Twitter/BTS_twt.csv",
                mode="w", newline="", encoding='utf-8-sig')
    writer = csv.writer(file)
    writer.writerow(["date", "text", "pic"])
    for twt in twts:
        writer.writerow(twt)
    return True


api = twitter.Api(consumer_key=twitter_consumer_key,
                  consumer_secret=twitter_consumer_secret,
                  access_token_key=twitter_access_token,
                  access_token_secret=twitter_access_token_secret)

account = "@BTS_twt"
result = api.GetUserTimeline(screen_name=account, count=200, include_rts=False, exclude_replies=True)
print(len(result))


# for twt in result:
#     print(changeDateFormat(twt.created_at))
#     print(twt.text)
#     if(twt.media):
#         # print(twt.media[0])
#         # print(twt.media[0].media_url_https)
#         print(len(twt.media))
#         pic_num = len(twt.media)
#         for i in range(pic_num):
#             print(twt.media[i].media_url_https)
#     print()
#     print()

twts = []
cnt = 1
for r in result:
    twt = []
    twt.append(changeDateFormat(r.created_at))
    twt.append(r.text)
    if(r.media):
        pic_num = len(r.media)
        for i in range(pic_num):
            pics = []
            pics.append(r.media[i].media_url_https)
        twt.append(pics)
    else:
        twt.append(None)
    twts.append(twt)
    cnt += 1
    print(cnt)

print(twts)
save_to_file(twts)
