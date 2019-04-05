from flask import Flask, render_template, request, redirect 
import os
import pymongo
import pymongo 
from pymongo import MongoClient


app = Flask(__name__)


MONGO_URL = os.environ.get('MONGOHQ_URL') 
client = MongoClient(MONGO_URL)
db = client.app129241652
collection = db.shoutouts


@app.route("/", methods=['GET']) 
def index(): 
	shouts = collection.find() 
	return render_template('index.html', shouts=shouts)

@app.route("/post", methods=['POST']) 
def post(): 
	shout = {"name":request.form['name'], "message":request.form['message']} 
	shout_id = collection.insert(shout) 
	return redirect('/')

@app.route("/deleteAll", methods=['GET']) 
def deleteAll(): 
	collection.remove()
	return redirect('/')
	
if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000)) 
	app.run(host='0.0.0.0', port=port)