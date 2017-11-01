#!/usr/bin/env python

#https://developers.google.com/api-client-library/python/
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
from tableCreate import TableObject


# [START Table Creater ]
def createTable(bigquery):
    tables = bigquery.tables()

    try:
        #insert utility make call to BQ API with payload (TableObject) contains schema and table-name information
        tableStatusObject = tables.insert(projectId='mimetic-slate', datasetId='BQ_Dataset', body=TableObject).execute()
        print "\n\nTable Created"
    except Exception as e:
        print "Table Creation Failed !! ", e
# [END]

def main():
    #to get credentials from my laptop
    credentials = GoogleCredentials.get_application_default()
    # Construct the service object for interacting with the BigQuery API.
    bigquery = discovery.build('bigquery', 'v2', credentials=credentials)
    createTable(bigquery)

if __name__ == '__main__':
    main()
    print "BQ Table Creator !!"
