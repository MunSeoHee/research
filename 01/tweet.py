import tweepy
from math import log10


def idf(t, D):
    # D is documents == document list
    numerator = len(D)
    denominator = 1 + len([ True for d in D if t in d])
    return log10(numerator/denominator)

def tfidf(t, d, D):
    return tf(t,d)*idf(t, D)

#문서 단어 빈도
def f(t, d):
    return d.count(t)

def tf(t, d):
    return 0.5 + 0.5*f(t,d)/max([f(w,d) for w in d])

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

category = ['#동물']
followingtweet=[]
categorylist=[]
usertweetlist=[]
followinglist = []
hashtaglist=[]
user_hashtag_tf=[]

#카테고리 별 해시태그 추출
keyword = "#동물"
#API.search(q, [geocode], [lang], [locale], [result_type], [count], [until], [since_id], [max_id], [include_entities])
search = api.search(keyword,lang="ko",count=100)
for tweet in search:
    for hashtag in tweet._json['entities']['hashtags']:
        categorylist.append(hashtag["text"])

# for t in categorylist:
#     print(f(t,categorylist))

#사용자 트윗
user = api.me()._json["id"]
usertweet = api.user_timeline(count="10")
for tweet in usertweet:
    for hashtag in tweet._json["entities"]['hashtags']:
        hashtaglist.append(hashtag['text'])


#팔로잉하는 유저 목록
#method:: API.friends([id/user_id/screen_name], [cursor], [skip_status], [include_user_entities])
friend = api.friends(id=user)
for f in friend:
    followinglist.append(f._json["id"])             



#팔로잉하는 유저의 트윗, 리트윗 
#method:: API.user_timeline([id/user_id/screen_name], [since_id], [max_id], [count], [page])
for following in followinglist:
    for tweet in api.user_timeline(following, count="15"):
        for hashtag in tweet._json["entities"]['hashtags']:
            hashtaglist.append(hashtag['text'])





for t in categorylist:
    print(0.5 + 0.5*categorylist.count(t)/max([categorylist.count(w) for w in categorylist]))

print("########")