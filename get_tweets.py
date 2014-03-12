from twitter import *
from models.twitter_employee import TwitterEmployee
from models.tweet import Tweet
import time

OAUTH_TOKEN = "YOUR_TWITTER_OAUTH_TOKEN"
OAUTH_SECRET= "YOUR_OAUTH_SECRET"
CONSUMER_KEY = "YOUR_CONSUMER_KEY"
CONSUMER_SECRET = "YOUR_CONSUMER_SECRET"

t = Twitter(
    auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
               CONSUMER_KEY, CONSUMER_SECRET)
    )

employees = TwitterEmployee.find()
num_employees = employees.count()
num_tweets = 0
curr_employee = 0
max_id_dict = {}

# Clear out all existing tweets.
Tweet.remove()

print "Starting Process at: ", time.localtime()
while num_tweets < 100000:
  # cycle over employees
  employee = employees[curr_employee % num_employees]
  sn = employee['screen_name']
  max_id = max_id_dict.get(sn,None)
  try:
    if max_id:
      tweets = t.statuses.user_timeline(screen_name=sn,count=200,max_id=max_id)
    else:
      tweets = t.statuses.user_timeline(screen_name=sn, count=200)
  except TwitterHTTPError, e:
    print "Error: ", e
    curr_employee += 1
    time.sleep(5)
    continue

  # save max_id for next query
  # subtract 1 because we have 64-bit ints
  # see: https://dev.twitter.com/docs/working-with-timelines
  if len(tweets) > 0:
    max_id_dict[sn] = tweets[-1]['id'] - 1
  for tweet in tweets:
    new_tweet = Tweet(retweet_count=tweet['retweet_count'],
                      favorites_count=tweet['favorite_count'],
                      created_at=tweet['created_at'],
                      twitter_id=tweet['id'],
                      text=tweet['text'],
                      user_id=employee['screen_name'])
    new_tweet.save()
    if '_id' in new_tweet:
      num_tweets += 1
  curr_employee += 1

  # user_timeline can be called 180 times every 15 minutes
  # so wait 5 seconds between calls so we don't hit rate limit
  time.sleep(5)
  print "Progress Report--\n", "\tTweets: ", num_tweets, "\n\tCurr User: ", sn

print "Completed at: ", time.localtime()






