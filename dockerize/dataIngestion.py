
# coding: utf-8

# In[2]:

import time, logging
import boto3,json
import datetime as dt

logfile=time.strftime('%d%m%Y') + ".log"
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',filename=logfile, datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.INFO)

#Load config file
config = json.load(open('config.json'))
accesskey =  config['AWSAccess']
secretkey = config['AWSSecret']


#Create a connection
s3 = boto3.resource('s3',
                    aws_access_key_id =  accesskey, 
                    aws_secret_access_key =  secretkey)
                   
#Create bucket if required
for bucket in s3.buckets.all():
    if bucket.name != 'ZillowData':
        s3.create_bucket(Bucket='ZillowData')
        logging.info('Bucket created')
        
#Upload data to bucket
file_to_upload = open("Clean.csv", 'rb')
s3.Bucket('ZillowData').put_object(Key="Clean.csv", Body=file_to_upload)
logging.info('Clean.csv File uploaded')

