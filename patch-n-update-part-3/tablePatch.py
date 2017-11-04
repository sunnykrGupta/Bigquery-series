#!/usr/bin/env python

#https://developers.google.com/api-client-library/python/
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
from schema import TableObject


# [START Table Creater ]
def PatchTable(bigquery):
    tables = bigquery.tables()

    try:
        #Updates information in an existing table. The update method replaces the entire table resource, whereas the patch method only replaces fields that are provided in the submitted table resource. This method supports patch semantics.
        tableStatusObject = tables.patch(projectId=TableObject['tableReference']['projectId'], datasetId=TableObject['tableReference']['datasetId'], tableId=TableObject['tableReference']['tableId'], body=TableObject).execute()
        print "\n\nTable Patched"
    except Exception as e:
        print "Patch Failed !! ", e
# [END]

def main():
    #to get credentials from my laptop
    credentials = GoogleCredentials.get_application_default()
    # Construct the service object for interacting with the BigQuery API.
    bigquery = discovery.build('bigquery', 'v2', credentials=credentials)
    PatchTable(bigquery)


'''
https://cloud.google.com/bigquery/docs/tables#update-schema
'''

if __name__ == '__main__':
    main()
    print "BQ Table Patch !!"
