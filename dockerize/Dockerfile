FROM python:3

RUN pip install jupyter
RUN pip install boto3
RUN pip install arrow
RUN pip install pandas 
RUN pip install  seaborn 

RUN mkdir /Assignment2

WORKDIR /Assignment2

EXPOSE 8888

ADD *.ipynb *.json /Assignment2/
ADD properties_2016.csv /Assignment2/
ADD train_2016_v2.csv /Assignment2/
ADD *.sh /Assignment2/
COPY . /Assignment2/

RUN chmod 755 /Assignment2/*

RUN chmod 755 /Assignment2/run.sh
CMD ["bash" , "/Assignment2/run.sh"]