# importing modules
from flask import Flask, request, jsonify, render_template

# declaring app name
app = Flask(__name__)

#connecting to app.py
from app import app

#importing dictionary
from dict import quotes

#creating routes
@app.route('/')
@app.route('/index') #homepage
def index():
    home = {'page': 'Welcome to January with Philosophy'}
    return render_template('index.html', title='Home', home=home, quotes=quotes)

@app.route('/overview') #January overview
def get_all_quotes():
    return render_template('januaryoverview.html', title='January Overview', quotes=quotes)

@app.route("/quotes", methods=["GET"]) #whole jsonify list 
def get_quotes():
    return jsonify(quotes)

@app.route("/quotes/<id>")  #jsonify view for single quote
def get_quote_by_id(id):
    for quote in quotes:
        if quote["id"] == int(id):
            return jsonify(quote)
    return jsonify()

@app.route('/date/<day>') #connecting every date to html's files in templates
def dateInJanuary(day):
    page = {'page': day + '.January'} 
    return render_template(day + '.html', title=page, page=page)
