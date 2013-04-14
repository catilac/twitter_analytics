from klout import *
from models.twitter_employee import TwitterEmployee

KLOUT_API_KEY = "48fv7bcbcc36s4fpuezm6uvs"

k = Klout(KLOUT_API_KEY)

employees = TwitterEmployee.find()

for employee in employees:
  sn = employee['screen_name']
  try:
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

