import sys
import os
from azure.storage.blob import BlobServiceClient

def list_files_with_sas(sas_url, account_url, container_name):
    blob_service_client = BlobServiceClient(account_url=account_url, credential=sas_url)

    container_client = blob_service_client.get_container_client(container_name)

    # List files in the container
    blob_list = container_client.list_blobs()

    # Print the names of the files
    print(f"Files in the '{container_name}' container:")
    for blob in blob_list:
        print(blob.name)

# Replace values with your actual SAS URL, account URL and container name
account_url=sys.argv[1]
sas_token=sys.argv[2]
container_name = account_url.rsplit('/',1)[1]
account_url = account_url.rsplit('/',1)[0]

list_files_with_sas(sas_token, account_url, container_name)