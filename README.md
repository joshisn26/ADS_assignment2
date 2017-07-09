# ADS_assignment2
ADS_assignment2
To execute the code follow this steps:

1. pull docker image from https://hub.docker.com/r/vipshah/ads-assignment2/

docker pull vipshah/ads-assignment2:final

2. Create new container

docker create --name='containername' vipshah/ads-assignment2:final

3. Run the container

docker start -i containername

This will upload a clean file in Amazon s3 bucket. and it will print done message.
