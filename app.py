import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    api_key=os.environ['GOOGLE_CALENDAR_API_KEY']
    return render_template("index.html", api_key=api_key)

if __name__ == '__main__':
    app.run()
