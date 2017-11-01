#!/usr/bin/env python

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

import json, time, copy
import redis


batchCount = 100

redisStream = redis.Redis(host='127.0.0.1',
             port='6379',
            password='')

streamObject = {
    "rows": [
      #{ "json": {# Represents a single JSON object. } }
    ],
 }

#[START Streaming batcher]
def streamBuilder():
    #Contains list of json object
    newStreamObject = copy.deepcopy(streamObject)

    currentCounter = 0
    while currentCounter < batchCount:
        try:
            packet = redisStream.brpop("redisList",  timeout=0)[1]
            newStreamObject["rows"].append({"json" : json.loads(packet) })
            currentCounter +=  1
        except Exception as e:
            print "Exception while BRPOP Redis  : ", str(e)
            time.sleep(2)

    #print json.dumps(newStreamObject, indent=4)
    return newStreamObject
#[END]


# [START Streaming Utility]
def streamUtils(bigquery):
    tabledata = bigquery.tabledata()

    #Run infinitely
    while True:
        streamBuildBatch = streamBuilder()
        try:
            #BQ API to insert bulk data into table
            insertStatusObject = tabledata.insertAll(projectId='mimetic-slate', datasetId='BQ_Dataset', tableId='StreamTable', body=streamBuildBatch).execute()

            print "STREAMING -- ", insertStatusObject

            if "insertErrors" in insertStatusObject:
                 print insertStatusObject

        except Exception as e:
            print "Exception while insertion : ", str(e)

# [ MAIN]
def main():
    credentials = GoogleCredentials.get_application_default()
    # Construct the service object for interacting with the BigQuery API.
    bigquery = discovery.build('bigquery', 'v2', credentials=credentials)

    #Stream utility
    streamUtils(bigquery)
# [END]

'''
RESOURCES : https://developers.google.com/resources/api-libraries/documentation/bigquery/v2/python/latest/bigquery_v2.tabledata.html
'''

if __name__ == '__main__':
    main()
