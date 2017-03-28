from flask import Flask
from flask import render_template, url_for

import parse_data

app = Flask(__name__)


@app.route("/dashboard")
def dashboard():
    data = parse_data.load_and_format_data()

    title = 'Grand Bargain Monitoring'

    return render_template('dashboard.html', data=data, heading=title, page_title=title)


if __name__ == "__main__":
    app.run()
