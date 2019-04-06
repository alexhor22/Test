from flask import Flask, render_template, request, redirect 
import os
import pymongo
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

# @app.route("/changeStatus", methods=['POST']) 
# def post(): 
# 	shout = {"status":request.form['status'], "adress":"", "name":""} 
# 	shout_id = db['Tec'].insert(shout) 
# 	return redirect('/')

# @app.route("/createNew", methods=['POST']) 
# def createNew(): 
# 	shout = {"status":0, "adress":"", "name":""}
# 	shout_id = db[request.form['colonia']].insert(shout)
# 	return redirect('/')
	
if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000)) 
	app.run(host='0.0.0.0', port=port)