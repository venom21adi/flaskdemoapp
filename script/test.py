from azure.storage.blob import *
accountName = "flaskdemoappstorage"
accountKey = "prbvCQU0nU+u3/Svm8rL/+r3HZWUlSkzu7T5xHg8ihe3U08wxL+eQTC8PVIvf/AmQMHFbiJCufmA+AStoGmxGw=="
containerName = "flaskdemoappcontainer"
sas_Token ="sp=racwdli&st=2023-05-25T15:25:32Z&se=2023-05-25T23:25:32Z&spr=https&sv=2022-11-02&sr=c&sig=OSBDUVh8Pkg%2FHaZae%2BjIh0v5dphn1T3Eq42Mc3wusnk%3D"
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

    blobService = BlockBlobService(account_name=accountName, sas_token =sas_Token)

    #blobService.create_blob_from_text(containerName, 'Test', output)

    
