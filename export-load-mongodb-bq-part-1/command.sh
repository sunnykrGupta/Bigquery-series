

#mongoimport reference
https://docs.mongodb.com/manual/reference/program/mongoimport/

#mongoexport reference
https://docs.mongodb.com/manual/reference/program/mongoexport/

#BQ Dataset Creation
$ bq mk -d --data_location=US   BQ_Dataset
// Verify your dataset creation
$ bq ls
    datasetId
 ----------------
  BQ_Dataset

#https://cloud.google.com/bigquery/docs/datasets#create-dataset


#BQ load
$ bq load --project_id=mimetic-slate-179915   \
    --source_format=NEWLINE_DELIMITED_JSON --max_bad_records 10 \
    BQ_Dataset.Restaurant ./restaurant.json  /restaurantSchema.json
#https://cloud.google.com/bigquery/bq-command-line-tool#creatingtablefromfile

#BQ Show
$ bq show BQ_Dataset.Restaurant
#https://cloud.google.com/bigquery/bq-command-line-tool#tables

#Create Storage bucket
#//to create Cloud storage bucket for this example.
$ gsutil mb  gs://bq-storage

#//to verify bucket creation
$ gsutil ls
gs://bq-storage/
#https://cloud.google.com/storage/docs/creating-buckets

#//Run command to upload
$ gsutil cp restaurant.json gs://bq-storage/restaurant.json
#https://cloud.google.com/storage/docs/gsutil/commands/cp


#for running SQL Query in BQ
#https://cloud.google.com/bigquery/docs/reference/standard-sql/
