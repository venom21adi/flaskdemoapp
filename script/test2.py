from azure.storage.blob import *
accountName = "flaskdemoappstorage"
accountKey = "prbvCQU0nU+u3/Svm8rL/+r3HZWUlSkzu7T5xHg8ihe3U08wxL+eQTC8PVIvf/AmQMHFbiJCufmA+AStoGmxGw=="
containerName = "flaskdemoappcontainer"
sas_Token ="?sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2023-05-25T23:34:36Z&st=2023-05-25T15:34:36Z&spr=https&sig=wFfO5qt6ZdMQWL5H5FxcVPtFSNBcr5p1jQrHfjdKi8g%3D"

conn_str = "DefaultEndpointsProtocol=https;AccountName=flaskdemoappstorage;AccountKey=prbvCQU0nU+u3/Svm8rL/+r3HZWUlSkzu7T5xHg8ihe3U08wxL+eQTC8PVIvf/AmQMHFbiJCufmA+AStoGmxGw==;EndpointSuffix=core.windows.net"
#blobName = "test3.json"
import pandas as pd
lst =[]

def test2():
    for i in range(10):
        lst.append(i)
        
    return lst

def test():

    lst = test2()
    
    df = pd.DataFrame(lst)

    output = df.to_csv("Test.csv")

    blobService = BlockBlobService(account_name=accountName,account_key =accountKey)

    #blobService.create_blob_from_text(containerName, 'Test', output)

    
