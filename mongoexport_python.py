import pymongo
import sys
import csv

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.test
col=db.longIntTest

try:
  cursor = col.find({},{'_id':0})
except Exception as e:
  print "Unexpected error:", type(e), e

with open('longIntTest_python.csv', 'w') as csvfile:
  fieldnames = ['c1', 'c2','c3','c4']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()
  for doc in cursor:
    print doc
    writer.writerow(doc)