import sys
import requests
import json
import os

def load_dotenv(path: str = ".env") -> None:
    if not os.path.exists(path):
        return
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            key, value = line.split("=", 1)
            os.environ[key] = value

def get_job_definition():
    # load job definition from json file
    job_def = json.load(open('job-definition.json'))
    return json.dumps(job_def)

if __name__ == "__main__":
    # load host and access token from .env config
    load_dotenv()
    host = os.environ['TASK_URL']
    token = os.environ['ACCESS_TOKEN']

    create_job_response = requests.post(host + '/api/2.1/jobs/create',
                                        data = get_job_definition(),
                                        auth = ("token", token))

    job_id = json.loads(create_job_response.content.decode('utf-8'))['job_id']
    print(f"Successfully completed job ID: {job_id}")

