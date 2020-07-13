from flask import Flask, render_template, jsonify, request
from babel import numbers, dates
from datetime import date, datetime, time
from flask_babel import Babel, format_decimal, format_date, gettext

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

@babel.localeselector
def get_locale():
    return 'zh'
    # return request.accept_languages.match(['en', 'es', de'])

@app.route('/')
def index():
    anthony = gettext('Anthony')

    num = format_decimal(12345)

    d = date(2020, 7, 13)

    day = format_date(d)

    results = {'num' : num, 'date' : day}
    return render_template('index.html', results = results, anthony = anthony)

if __name__ == '__main__':  
    app.run('0.0.0.0', port=5000, debug=True)