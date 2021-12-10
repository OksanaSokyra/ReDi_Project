from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
from app import app
from dict import quotes


@app.route('/')
@app.route('/index')
def index():
    home = {'page': 'Welcome to January with Philosophy'}
    return render_template('index.html', title='Home', home=home, quotes=quotes)

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

@app.route('/date/1')
def date1():
    page = {'page': '01.January'}
    return render_template('1.html', title=page, page=page)

@app.route('/date/2')
def date2():
    page = {'page': '02.January'}
    return render_template('2.html', title=page, page=page)

@app.route('/date/3')
def date3():
    page = {'page': '03.January'}
    return render_template('3.html', title=page, page=page)

@app.route('/date/4')
def date4():
    page = {'page': '04.January'}
    return render_template('4.html', title=page, page=page)

@app.route('/date/5')
def date5():
    page = {'page': '05.January'}
    return render_template('5.html', title=page, page=page)

@app.route('/date/6')
def date6():
    page = {'page': '06.January'}
    return render_template('6.html', title=page, page=page)

@app.route('/date/7')
def date7():
    page = {'page': '07.January'}
    return render_template('7.html', title=page, page=page)

@app.route('/date/8')
def date8():
    page = {'page': '08.January'}
    return render_template('8.html', title=page, page=page)

@app.route('/date/9')
def date9():
    page = {'page': '09.January'}
    return render_template('9.html', title=page, page=page)

@app.route('/date/10')
def date10():
    page = {'page': '10.January'}
    return render_template('10.html', title=page, page=page)

@app.route('/date/11')
def date11():
    page = {'page': '11.January'}
    return render_template('11.html', title=page, page=page)

@app.route('/date/12')
def date12():
    page = {'page': '12.January'}
    return render_template('12.html', title=page, page=page)

@app.route('/date/13')
def date13():
    page = {'page': '13.January'}
    return render_template('13.html', title=page, page=page)

@app.route('/date/14')
def date14():
    page = {'page': '14.January'}
    return render_template('14.html', title=page, page=page)

@app.route('/date/15')
def date15():
    page = {'page': '15.January'}
    return render_template('15.html', title=page, page=page)

@app.route('/date/16')
def date16():
    page = {'page': '16.January'}
    return render_template('16.html', title=page, page=page)

@app.route('/date/17')
def date17():
    page = {'page': '17.January'}
    return render_template('17.html', title=page, page=page)

@app.route('/date/18')
def date18():
    page = {'page': '18.January'}
    return render_template('18.html', title=page, page=page)

@app.route('/date/19')
def date19():
    page = {'page': '19.January'}
    return render_template('19.html', title=page, page=page)

@app.route('/date/20')
def date20():
    page = {'page': '20.January'}
    return render_template('20.html', title=page, page=page)

@app.route('/date/21')
def date21():
    page = {'page': '21.January'}
    return render_template('21.html', title=page, page=page)

@app.route('/date/22')
def date22():
    page = {'page': '22.January'}
    return render_template('22.html', title=page, page=page)

@app.route('/date/23')
def date23():
    page = {'page': '23.January'}
    return render_template('23.html', title=page, page=page)

@app.route('/date/24')
def date24():
    page = {'page': '24.January'}
    return render_template('24.html', title=page, page=page)

@app.route('/date/25')
def date25():
    page = {'page': '25.January'}
    return render_template('25.html', title=page, page=page)

@app.route('/date/26')
def date26():
    page = {'page': '26.January'}
    return render_template('26.html', title=page, page=page)

@app.route('/date/27')
def date27():
    page = {'page': '27.January'}
    return render_template('27.html', title=page, page=page)

@app.route('/date/28')
def date28():
    page = {'page': '28.January'}
    return render_template('28.html', title=page, page=page)

@app.route('/date/29')
def date29():
    page = {'page': '29.January'}
    return render_template('29.html', title=page, page=page)

@app.route('/date/30')
def date30():
    page = {'page': '30.January'}
    return render_template('30.html', title=page, page=page)

@app.route('/date/31')
def date31():
    page = {'page': '31.January'}
    return render_template('31.html', title=page, page=page)
    