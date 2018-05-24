from flask import Flask


app = Flask(__name__)

num1 = 10

@app.route("/")
def index():
    return "index"


if __name__ == '__main__':
    app.run()