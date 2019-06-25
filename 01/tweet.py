import tweepy

import tweepy

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="lcjGSPnCBjKU8OpRwsD7M0FEO"
consumer_secret="nHF3Z2W2M8ArXAeJlhDXCbtRPUKkux3TGNlouWEHYB4wjmxHVt"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="817240287286214656-iRuqc9UzZW2sx6bwfoROtqoLZUmHAyA"
access_token_secret="VdAaqQpBDooYMEM5Vs2sArLqcUJmblQoZLpF8NmF1dtIH"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
# print(api.me().name)
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)


keyword = "#동물"
#API.search(q, [geocode], [lang], [locale], [result_type], [count], [until], [since_id], [max_id], [include_entities])
search = api.search(keyword,lang="ko",count=100)
# print(search)
list=[]

for tweet in search:
    for hashtag in tweet._json['entities']['hashtags']:
        list.append(hashtag["text"])

print(list)



# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
# api.update_status(status='Updating using OAuth authentication via Tweepy!')




#문서 단어 빈도
# def f(t,d): 
#     return float(article_entity_count_dict[d][t]) 

# def tf(t,d): 
#     return 0.5 + ((0.5) * f(t, d) / max([f(w, d) for w, c in article_entity_count_dict[d].iteritems()])) 
    
# def idf(t):
#     return math.log10(category_number_of_documents[entity_category_count_dict[t]] / len(entity_article_count_dict[t].keys()))
