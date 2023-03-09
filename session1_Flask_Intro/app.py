from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/articles"

mongo = PyMongo(app)
bcrypt = Bcrypt(app)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    return render_template("dashboard.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # bussiness logic
    if request.method == "POST":
        # accept data from frontend(form data) - > email and password
        email = request.form["email"]
        password = request.form["password"]

        # Check if that email is present in database or not
        found_user = mongo.db.users.find_one({"email": email})
        # print(found_user)
        if found_user:
            print("user found")
            # if email is present then compare password_hash from db with user's entered password
            is_password_matched = bcrypt.check_password_hash(
                found_user["password"], password
            )

            if is_password_matched:
                print("correct password")
                # if password also matched then login successfull and redirect to dashboard
                return redirect("/dashboard")
            else:
                print("incorrect password")

        else:
            print("no user found")

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
