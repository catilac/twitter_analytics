from klout import *
from models.twitter_employee import TwitterEmployee
import time

KLOUT_API_KEY = "YOUR_API_KEY_HERE"

k = Klout(KLOUT_API_KEY)

employees = TwitterEmployee.find()

for idx, employee in enumerate(employees):
  sn = employee['screen_name']
  try:
    if (idx + 1) % 10:
      time.sleep(1)
    kloutId = k.identity.klout(screenName=sn).get('id')
  except KloutHTTPError, e:
    print e
    continue

  try:
    score = k.user.score(kloutId=kloutId).get('score')
  except KloutHTTPError, e:
    print e
    continue
  print "@",sn,"'s Klout Score: ", score

  employee['klout_score'] = score
  employee.save()

