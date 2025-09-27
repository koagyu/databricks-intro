# load json from task definnition file
JOB_ID = $(databricks jobs create --json @job-definition.json)
echo "Successful run with JOB_ID: $JOB_ID"