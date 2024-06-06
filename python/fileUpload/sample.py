import sys
import os
from azure.storage.blob import BlobClient

upload_file_path=sys.argv[1]
url=sys.argv[2]
token=sys.argv[3]
filename=os.path.basename(upload_file_path)

sas_url=url+filename+"?"+token

client = BlobClient.from_blob_url(sas_url)

with open(upload_file_path,'rb') as data:
    client.upload_blob(data)

print("**file uploaded**")