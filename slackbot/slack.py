# Import Python Libraries

from sqlalchemy import create_engine
import requests
import logging
import time
from datetime import datetime
import os
import pymongo

# Wait for 15 seconds so the get_tweets.py has time to pull the tweets and etl.py has time to establish the postgres db
time.sleep(15)

# Set Global Variables

webhook_url = "https://hooks.slack.com/services/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"

# Establish a connection to the MongoDB server

client = pymongo.MongoClient(host="mongodb", port=27017)

# Select the database you want to use within the MongoDB server

db = client.twitter

# Create Postgres engine

pg = create_engine('postgresql://postgres:titanic22@postgresdb:5432/twitter', echo=True)

results = pg.execute('''SELECT * FROM tweets LIMIT 1''')

for t in results:
    print(t)
    data = {'text': t[0]}
    print(data)
    requests.post(url=webhook_url, json = data)