import pymongo
import time
from sqlalchemy import create_engine
import psycopg2

time.sleep(10)  # seconds

# Establish a connection to the MongoDB server
client = pymongo.MongoClient(host="mongodb", port=27017)

# Select the database you want to use withing the MongoDB server
db = client.twitter

pg = create_engine('postgresql://postgres:titanic22@postgresdb:5432/twitter', echo=True)

pg.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
    text VARCHAR(500)
);
''')

docs = db.tweets.find(limit=5)

for doc in docs:
    text = doc['text']
    query = "INSERT INTO tweets VALUES (%s);"
    pg.execute(query, (text))