import re
from datetime import datetime

from flask import Flask, render_template
import LineaRegressionExample
app = Flask (__name__)
@app.route("/")
def home():
    return "Hello Flask"
@app.route("/Hello/<name>")
def hello_there(name):
    now= datetime.now()
    formatted_now = now.strftime("%d/%m/y,%H:%M:%S")
    match_object = re.match("[a-zA-Z ]",name)
    if match_object:
        clean_name =match_object.group(0)
    else:
        clean_name= "friend"
    
    content = "Hello there,"+clean_name+ "!today is:"+ formatted_now
    return content

@app.route("/hello2")
def helloHTML():
  return render_template ("helloflask.html")