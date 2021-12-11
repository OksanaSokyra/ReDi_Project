#importing flask, dictionary etc.

from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
from app import app
from dict import quotes


#creating routes
@app.route('/')
@app.route('/index')
def index():
    home = {'page': 'Welcome to January with Philosophy'}
    return render_template('index.html', title='Home', home=home, quotes=quotes)

@app.route('/wholejanuary')
def get_all_quotes():
    return render_template('januaryoverview.html', title='January Overview', quotes=quotes)

def _find_next_id():
    return max(quote["id"] for quote in quotes) + 1

@app.route("/quotes", methods=["GET"])
def get_quotes():
    return jsonify(quotes)

@app.route("/quotes/<id>", methods=["GET"])
def get_quote_by_id(id):
    for quote in quotes:
        if quote["id"] == int(id):
            return jsonify(quote)
    return jsonify()

@app.route("/quotes", methods=["POST"])
def add_quote():
    if request.is_json:
        quote = request.get_json()
        quote["id"] = _find_next_id()
        quotes.append(quote)
        return quote, 201
    return {"error": "Request must be JSON"}, 415

@app.route('/date/<day>')
def dateInJanuary(day):
    page = {'page': day + '.January'} # todo add padding zero
    return render_template(day + '.html', title=page, page=page)
