
#### Streaming with Redis - BigQuery Part-II
[https://sunnykrgupta.github.io/streaming-with-redis-bigquery-part-ii.html](https://sunnykrgupta.github.io/streaming-with-redis-bigquery-part-ii.html)


#### Redis LPUSH reference

https://redis.io/commands/lpush

#### Redis BRPOP reference

https://redis.io/commands/brpop



#### BQ Dataset Creation
```
$ bq mk -d --data_location=US   BQ_Dataset
// Verify your dataset creation
$ bq ls
    datasetId
 ----------------
  BQ_Dataset
```
[https://cloud.google.com/bigquery/docs/datasets#create-dataset](https://cloud.google.com/bigquery/docs/datasets#create-dataset)

#### BQ Show
```
$ bq show BQ_Dataset.Restaurant
```
[https://cloud.google.com/bigquery/bq-command-line-tool#tables](https://cloud.google.com/bigquery/bq-command-line-tool#tables)

#### For running SQL Query in BQ
[https://cloud.google.com/bigquery/docs/reference/standard-sql/](https://cloud.google.com/bigquery/docs/reference/standard-sql/)
