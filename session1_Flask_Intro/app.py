from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/articles"

mongo = PyMongo(app)
bcrypt = Bcrypt(app)


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

        password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

        mongo.db.users.insert_one(
            {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "password": password_hash,
                "phone_number": phone_number,
                "city": city,
            }
        )

        return render_template("signup.html")

    print("its an get call")
    return render_template("signup.html")


@app.route("/bye")
def bye():
    return "Bye tata khatam"


if __name__ == "__main__":
    app.run(debug=True)
