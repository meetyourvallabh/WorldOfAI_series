from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/login")
def login():
    # bussiness logic
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    # Bussiness logic
    if request.method == "POST":
        print("its a post call")
        print(request.form["first_name"])
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        password = request.form["password"]
        phone_number = request.form["phone_number"]
        city = request.form["city"]

        print(first_name, email, password)
        return render_template("signup.html")

    print("its an get call")
    return render_template("signup.html")


@app.route("/bye")
def bye():
    return "Bye tata khatam"


if __name__ == "__main__":
    app.run(debug=True)
