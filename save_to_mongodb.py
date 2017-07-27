import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.crawler


record = {
  "name": "Andy",
  "rating": 1,
  "score": 1,
  "job": "it engineer"
}
record["age"] = 35

db.crawler.update_one(
  {"name": "Andy"},
  {"$set": {"gender": "male"}},
  upsert=True)