from flask import Flask, render_template, request, redirect, jsonify 
import os
import pymongo
from pymongo import MongoClient


app = Flask(__name__)

# heroku_55k7w1dv

MONGO_URL = os.environ.get('MONGODB_URI') 
client = MongoClient(MONGO_URL)
db = client.heroku_55k7w1dv
collection = db.TEST


@app.route("/", methods=['GET']) 
def index(): 
	return render_template('index.html')

@app.route("/off", methods=['GET']) 
def off(): 
	find = { "Lugar": "cuarto" }
	values = { "$set": {
	      "Lugar": "cuarto",
	      "status": 0
	      } }
	shout_id = collection.update_one(find,values) 
	return redirect('/')

@app.route("/on", methods=['GET']) 
def on(): 
	find = { "Lugar": "cuarto" }
	values = { "$set": {
	      "Lugar": "cuarto",
	      "status": 1
	      } }
	shout_id = collection.update_one(find,values) 
	return redirect('/')
	
if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000)) 
	app.run(host='0.0.0.0', port=port)