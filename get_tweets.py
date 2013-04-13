from twitter import *
from twitter_employee import TwitterEmployee
from tweet import Tweet
import time

twits = TwitterEmployee.find()
num_tweets = 0

for twit in twits:
