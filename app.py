from flask import *
import os
#from azure.storage.blob import BlobServiceClient
app = Flask(__name__)


"""
blob_service_client = BlobServiceClient.from_connection_string(conn_str=connect_str) # create a blob service client to interact with the storage account
try:
    container_client = blob_service_client.get_container_client(container=container_name) # get container client to interact with the container in which images will be stored
    container_client.get_container_properties() # get properties of the container to force exception to be thrown if container does not exist
except Exception as e:
    print(e)
    #print("Creating container...")
    #container_client = blob_service_client.create_container(container_name) # create a container in the storage account if it does not exist
"""
@app.route('/')
def index():
    return render_template('index.html')
    
    
@app.route('/page2')
def page2():
    from script.test import test
    test()
    #y = str(os.getcwd())
    return "Executed"  
    
@app.route('/page3')  
def page3():
    #from script.test import test
    #test()
    #y = str(os.getcwd())
    return render_template('page3.html') 
"""
@app.route('/')
def index():
    return "Hello World!"
"""
   

if __name__ == "__main__":
    app.secret_key = "ThisisNotASecret:p"
    app.run(debug=True)