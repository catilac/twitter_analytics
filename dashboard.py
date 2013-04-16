from flask import Flask
from flask import render_template
from pymongo import MongoClient
from bson.son import SON
from bson import json_util
import json

app = Flask(__name__)

client = MongoClient()
db = client.addvocate_exam
Tweets = db.tweets
Employees = db.twitter_employees

@app.route("/")
def dashboard():
  return render_template("dashboard.html")

@app.route("/top-users.json")
def top_users():
  top_users =  Tweets.aggregate([
      {"$group": {
        "_id": "$user_id", 
        "total_rts": {"$sum": "$retweet_count"}, 
        "total_fav": {"$sum": "$favorites_count"}}},
      {"$sort": SON([("total_rts", -1), ("total_fav", -1)])}
    ])
  return json.dumps(top_users['result'], default=json_util.default)


@app.route("/top-content.json")
def top_content():
  top_content = Tweets.find().sort("retweet_count", -1).sort("favorites_count", -1).limit(15)
  results = []
  for tweet in top_content:
    results.append(tweet)
  return json.dumps(results, default=json_util.default)

if __name__ == "__main__":
  app.run(debug=True)
