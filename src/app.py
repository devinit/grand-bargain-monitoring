from flask import Flask
from flask import render_template, url_for

import parse_data

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello World!"


@app.route("/dashboard")
def dashboard():
    data = parse_data.load_and_format_data()

    title = 'Grand Bargain Monitoring'

    return render_template('dashboard.html', data=data, heading=title, page_title=title)


# @app.route("/")
# def dashboard():
#     url_for('static', filename='style.css')

#     return render_template('base.html')


if __name__ == "__main__":
    app.run()
