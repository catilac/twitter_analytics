from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient()
db = client.addvocate_exam
Tweets = db.tweets
Employees = db.twitter_employees

@app.route("/top-users")
def top_users():
  top_users =  Tweets.aggregate({
      "$group": { 
        "_id": "$user_id", 
        "total_rts": { "$sum": "$retweet_count"}, 
        "total_fav": {"$sum": "$favorites_count"}}})
  return str(top_users)


@app.route("/top-content")
def top_content():
  top_content = Tweets.find() .sort("retweet_count", -1) .sort("favorites_count", -1).limit(15)
  print 'debug: ', top_content
  results = ''
  for tweet in top_content:
    results += str(tweet)
  return results

if __name__ == "__main__":
  app.run()
