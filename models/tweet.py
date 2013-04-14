from mongo import Document, Index

class Tweet(Document):
  """Twitter Tweet"""
  __database__ = 'addvocate_exam'
  __collection__ = 'tweets'
  __indexes__ = [
    Index('retweet_count'),
    Index('favorites_count'),
    Index('user_id'),
    Index('created_at'),
    Index('twitter_id', unique=True, sparse=True)
  ]
