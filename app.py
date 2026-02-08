from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/biography")
def biography():
    return render_template("biography.html")

@app.route("/monuments")
def monuments():
    return render_template("monuments.html")

@app.route("/textbooks")
def textbooks():
    return render_template("textbooks.html")

@app.route("/maps")
def maps():
    return render_template("maps.html")

if __name__ == "__main__":
    app.run()
