from flask import Flask,jsonify,request
from flask_cors import CORS,cross_origin
from services.db import mydb
import services.create_room
import json
app= Flask(__name__)



@app.route('/')
def index():
    print("hello")
    return "<h1> Welcome To Devils World!</h1>"

@app.route("/create",methods=['POST'])
@cross_origin(origin="*")
def create_room1():
    print("data is ",request)
    data=request.json
    response=services.create_room.create_room(mydb,data)
    print("Room created",response) 
    return response
