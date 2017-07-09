
from flask import Flask, render_template, request, json
import os
from pymongo import MongoClient
from bson import json_util
import pandas as pd
import logging
from geopy.distance import vincenty
logging.basicConfig(filename='log_filename.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filemode='w')


app = Flask(__name__)

# insert your connection details here

MONGO_URL = 'mongodb://joshisn:<password>@cluster0-shard-00-00-0phxm.mongodb.net:27017,cluster0-shard-00-01-0phxm.mongodb.net:27017,cluster0-shard-00-02-0phxm.mongodb.net:27017/DB?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin'

# connect to the MongoDB server

client = MongoClient(MONGO_URL)
print(client)
# connect to the default database within the server

db = client["DB"]


# On Bluemix, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8080
#port = int(os.getenv('PORT', 8080))

@app.route('/')
def home():
    return render_template('index.html')

# /* Endpoint to greet and see properties from given latitude.


@app.route('/api/visitors', methods=['GET', 'POST'])
def get_visitor():
	logging.info("Inside method")
	logging.info("**************************")
	c = float(request.form['lat'])
	d = float(request.form['lon'])
	lc= c-0.00005
	hc= c+0.00005
	logging.info("lc"+ str(lc))
	ld= d-0.00010
	hd= d+0.00010
	logging.info(str(ld)+"ld")
	collection = db.abc.find({'latitude':  { '$gt' : lc , '$lt' : hc }})
	collection1 = db.abc.find({'longitude':  { '$gt' : ld , '$lt' : hd }})
	p={}
	q={}
	o = (c, d)
	for a in collection:
		n = (a['latitude'], a['longitude'])
		p[a['parcelid']]=vincenty(o, n).miles
	for b in collection1:
		n= (b['latitude'],b['longitude'])
		q[b['parcelid']] =vincenty(o, n).miles
	z = {**p, **q}
	z1=sorted(z.items(), key=lambda value: value[1])
	
	logging.info("json"+json.dumps(z1[:10]))
	return render_template('index.html' , pi =json.dumps(z1[:10]))


if __name__ == '__main__':
	port = int(os.environ.get("VCAP_APP_PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=True)
