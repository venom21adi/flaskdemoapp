from azure.storage.blob import *
accountName = "flaskdemoappstorage"
accountKey = "prbvCQU0nU+u3/Svm8rL/+r3HZWUlSkzu7T5xHg8ihe3U08wxL+eQTC8PVIvf/AmQMHFbiJCufmA+AStoGmxGw=="
containerName = "flaskdemoappcontainer"
sas_Token ="?sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2023-05-25T23:34:36Z&st=2023-05-25T15:34:36Z&spr=https&sig=wFfO5qt6ZdMQWL5H5FxcVPtFSNBcr5p1jQrHfjdKi8g%3D"

conn_str = "DefaultEndpointsProtocol=https;AccountName=flaskdemoappstorage;AccountKey=prbvCQU0nU+u3/Svm8rL/+r3HZWUlSkzu7T5xHg8ihe3U08wxL+eQTC8PVIvf/AmQMHFbiJCufmA+AStoGmxGw==;EndpointSuffix=core.windows.net"
#blobName = "test3.json"
import pandas as pd
lst =[]
lst2 = []

def test2():
    for i in range(10):
        lst.append(i)
        lst2.append(i**2)
    value = [lst,lst2]
    df = pd.DataFrame(value)
    df = df.T
    return df

def test():
    # create data
    #head = ["col1" , "col2" , "col3"]
    #value = [[1 , 2 , 3],[4,5,6] , [8 , 7 , 9]]
    #df = pd.DataFrame (value, columns = head)
    #output = df.to_csv (index=False, encoding = "utf-8")
    #print(output)
    df = test2()
    
    
    #df = pd.DataFrame(lst1)

    output = df.to_csv(index = False,encoding="utf-8")

    connection_string=conn_str
    # Instantiate a new BlobServiceClient using a connection string
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    # Instantiate a new ContainerClient
    container_client = blob_service_client.get_container_client('mycsv2')
    try:
       # Create new Container in the service
       container_client.create_container()
       properties = container_client.get_container_properties()
    except ResourceExistsError:
       print("Container already exists.")

    # Instantiate a new BlobClient
    blob_client = container_client.get_blob_client("output.csv")
    # upload data
    blob_client.upload_blob(output, blob_type="BlockBlob")

    
