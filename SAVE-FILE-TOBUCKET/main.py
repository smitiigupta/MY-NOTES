#https://dzone.com/articles/upload-files-to-google-cloud

import os, sys
import json
import requests
from datetime import datetime, timezone
from google.cloud import storage
from google.oauth2 import service_account


credentials_dict = {
  "type": "service_account",
  "project_id": "",
  "private_key_id": "",
  "private_key": "",
  "client_email": "iam.gserviceaccount.com",
  "client_id": "",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/iam.gserviceaccount.com"
}
    

def save_file_to_bucket():

    try:

        credentials = service_account.Credentials.from_service_account_info(credentials_dict)
        client = storage.Client(project='oneasia', credentials=credentials)
        bucket_name = 'test_bucket_file_save'
        bucket = client.get_bucket(bucket_name)
        object_name_in_gcs_bucket = bucket.blob('my_first_gcs_upload.png')
        object_name_in_gcs_bucket.upload_from_filename('diwali.jpeg')
    
    except Exception as error:
        print("Line number of error is {}".format(sys.exc_info()[-1].tb_lineno), error)


save_file_to_bucket()