from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ddos")
@app.route("/")
def ddos():
    return render_template("ddos.html")


if __name__ == '__main__':
    app.run(debug=True)
