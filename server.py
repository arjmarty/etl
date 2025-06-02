from flask import Flask, jsonify, request
from datetime import timedelta, datetime as dt 
import pandas as pd

app = Flask(__name__)

@app.route("/home")
def no_display():
  num = number_display()
  return jsonify(num)
