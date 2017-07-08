
from flask import Flask, render_template, request, jsonify
import os
from pymongo import MongoClient
from bson import json_util
import pandas as pd

app = Flask(__name__)

# insert your connection details here

MONGO_URL = 'mongodb://joshisn:<PASSWORD>@cluster0-shard-00-00-0phxm.mongodb.net:27017,cluster0-shard-00-01-0phxm.mongodb.net:27017,cluster0-shard-00-02-0phxm.mongodb.net:27017/DB?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin'

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
	print("Inside method")
	c = float(request.form['lat'])
	print(c)
	p=[]
	collection = db.abc.find({'latitude': c}).limit(5)
	#a = collection['parcelid']
	print(collection)
	for a in collection:
		p.append(a['parcelid'])
	print(p)
	return render_template('index.html' , pi = p)


if __name__ == '__main__':
	port = int(os.environ.get("VCAP_APP_PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=True)
