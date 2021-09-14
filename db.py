
from google.cloud.sql.connector import connector
from pymongo import MongoClient

def get_connect_cloudSql():
    conn = connector.connect(
    "istdsa-deneme:europe-west1:users-db",
    "pymysql",
    user="root",
    password="****",
    db='users',)
    return conn

def get_connect_mongoDB():
    connect_db = "mongodb+srv://username:******@cluster0.kck47.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    cluster = MongoClient(connect_db)
    return cluster
