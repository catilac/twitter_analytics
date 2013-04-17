from twitter import *
from models.twitter_employee import TwitterEmployee
import time

OAUTH_TOKEN = "16999900-Egp9CoOFvp5tGnea7mCAKjxJ77lRiVlrt4vfiRPYZ"
OAUTH_SECRET= "0yXs7yomSsZlXdVDKIO7L7fuWBMn1pmMYB1wbw5E9eM"
CONSUMER_KEY = "uFuIq77xQTgrCXhAj4ugDw"
CONSUMER_SECRET = "MJKUc3IyN5aztJCrQ8kTI708mPao76dSNGONZ6P6I"

t = Twitter(
    auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
               CONSUMER_KEY, CONSUMER_SECRET)
    )

# Clear out existing employees
TwitterEmployee.remove()

# Grab all the users from the team list
cursor = -1
while cursor != 0:
  print "Current Page: ", cursor
  try:
    twitter_team_list = t.lists.members(cursor=cursor, slug="team", owner_screen_name="twitter")
  except TwitterHTTPError, e:
    if e['errors']['code'] == 88:
      print "Rate Limit...waiting 15 min"
      time.sleep(60 * 15)  
    else:
      raise
  else:
    cursor = twitter_team_list['next_cursor']
    twitter_employees = twitter_team_list['users']
    # create a TwitterEmployee entry for each user
    for employee in twitter_employees:
      screen_name = employee['screen_name']
      twit = TwitterEmployee(screen_name=name)
      twit.save()

print 'Number of Users: ', TwitterEmployee.count()
