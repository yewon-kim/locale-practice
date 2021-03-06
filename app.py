from flask import Flask, render_template, jsonify, request
from datetime import date, datetime, time
from flask_babel import Babel, format_decimal, format_date, gettext

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

@babel.localeselector
def get_locale():
    # return 'es'
    return request.accept_languages.best_match(['en', 'es', 'de', 'ko'])

@app.route('/')
def index():
    anthony = gettext(u'Anthony')

    num = format_decimal(12345)

    d = datetime.fromtimestamp(1594460958.12345)

    day = format_date(d)

    results = {
        'num' : num, 
        'date' : day, 
        'anthony' : anthony
    }
    return render_template('index.html', results = results)

if __name__ == '__main__':  
    app.run('0.0.0.0', port=5000, debug=True)