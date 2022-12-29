import pymongo
import pandas as pd 
import json 
from sensor.config import mongo_client


DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME = "aps"
COLLECTION_NAME = 'sensor'

if __name__ == '__main__':
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    # Convert dataframe to json so that we can dumpy these record in mongodb
    df.reset_index(drop=True, inplace=True)
    json_records = list(json.loads(df.T.to_json()).values())
    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records)
