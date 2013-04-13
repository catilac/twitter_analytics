from mongo import Document, Index

class TwitterEmployee(Document):
  """Twitter Employee"""
  __database__ = 'addvocate_exam'
  __collection__ = 'twitter_employees'
  __indexes__= [Index('screen_name', unique=True, sparse=True)]
