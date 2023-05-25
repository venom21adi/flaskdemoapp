from azure.storage.blob import (
    BlockBlobService
)
accountName = "flaskdemoappstorage"
accountKey = "prbvCQU0nU+u3/Svm8rL/+r3HZWUlSkzu7T5xHg8ihe3U08wxL+eQTC8PVIvf/AmQMHFbiJCufmA+AStoGmxGw=="
containerName = "flaskdemoappcontainer"
#blobName = "test3.json"
#
lst =[]

def test():
    for i in range(10):
    lst.append(i)
    return lst
    
import pandas as pd

df = pd.DataFrame(lst)

output = df.to_csv("Test.csv")

blobService = BlockBlobService(account_name=accountName, account_key=accountKey)

#blobService.create_blob_from_text('test1', 'Test.csv', output)