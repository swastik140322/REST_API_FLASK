# Author: Yash Pal Singh
# Version: V1.1
# Date: 11/29/2023
# Purpose: To write my first REST API Flask contents using FLASK for Web Deveelopment and REST API for Access using Python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
