from flask import Flask, render_template

app = Flask(__name__)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/bye")
def bye():
    return "Bye tata khatam"


if __name__ == "__main__":
    app.run(debug=True)
