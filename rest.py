#main.py
from flask import Flask, jsonify, request
from db import get_connect_cloudSql,get_connect_mongoDB

app = Flask(__name__)

@app.route('/insert', methods=['POST', 'GET'])
def add_data_cloud():
    if request.method == 'POST':
        conn = get_connect()
        cnx = conn.cursor()
        username = request.form['username']
        password = request.form['password']
        cnx.execute("INSERT INTO user VALUES("+username+",PASSWORD("+password+"))")
        return "<p>Succesful!</p>"
    elif request.method == "GET":
        return "<p>Hello, World!</p>"

@app.route('/insertMongo', methods=['POST', 'GET'])
def add_data_mongo():
    if request.method == 'POST':
        conn = get_connect_mongoDB()
        myDB = conn["airbnbDB"]
        mycol = myDB["airbnb"]
        rawdata = request.json
        mycol.insert_one(rawdata)
        return "<p>Succesful!</p>"
    elif request.method == "GET":
        return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run()
