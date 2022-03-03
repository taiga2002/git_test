from tokenize import String
from flask import Flask, request

app = Flask(__name__)
@app.route("/hello-json")
def hello_json():
    return {"text": "Hello World from Dictionary"}
@app.route("/hello-html")
def hello_html():
    return "<h1>Hello World</h1><p>Subtext</p>"

@app.route("/hello")
def index():
    name = request.args.get("name")
    if name:
        return "Hello " + str(name)
    else:
        return "Hello World"

# how to change @app.route("/hello?name = [name]")
@app.route("/hello/<name>")
def whatevername(name):
    return "Hello" + str(name)

@app.route("/hello/<name>/<num>")
def money_exchange(name, num):
    return "Hello" + str(name) + "your change is " + str(10-num)

@app.route("/reflect")
def reflect():
    data = request.data
    return data
@app.route("/reflect/plex")
def reflect_plex():
    new_dictionary = {}
    data = request.json
    print(data)
    for i in data.keys():
        new_dictionary["plex_" + str(i)] = data[i]
    return new_dictionary

app.run(host = "0.0.0.0", port = 81, debug = True)
      
    
   


