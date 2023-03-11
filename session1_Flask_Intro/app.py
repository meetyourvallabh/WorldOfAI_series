from flask import Flask, render_template, request, redirect, flash, session, url_for
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
import random
from functools import wraps
import uuid

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/articles"

mongo = PyMongo(app)
bcrypt = Bcrypt(app)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "is_user_logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Unauthorised access", "warning")
            return redirect(url_for("login"))

    return decorated_function


@app.route("/", methods=["GET"])
def index():
    articles = mongo.db.articles.find()
    return render_template("index.html", articles=articles)


@app.route("/view_article/<id>", methods=["GET", "POST"])
def view_article(id):
    article = mongo.db.articles.find_one({"id": id})
    return render_template("view_article.html", article=article)


@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    # get all articles of current user
    articles = mongo.db.articles.find({"author_email": session["email"]})
    return render_template("dashboard.html", articles=articles)


@app.route("/add_article", methods=["GET", "POST"])
@login_required
def add_article():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        # id = random.randint(11111, 99999)
        id = str(uuid.uuid4())
        author = session["first_name"] + " " + session["last_name"]
        author_email = session["email"]
        mongo.db.articles.insert_one(
            {
                "title": title,
                "content": content,
                "id": id,
                "author": author,
                "author_email": author_email,
            }
        )

        flash("Article submitted", "success")
    return render_template("add_article.html")


@app.route("/edit_article/<id>", methods=["GET", "POST"])
@login_required
def edit_article(id):

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        mongo.db.articles.update_one(
            {"id": id}, {"$set": {"title": title, "content": content}}
        )
        flash("Article edited successfully", "success")

    article = mongo.db.articles.find_one({"id": id})
    return render_template("edit_article.html", article=article)


@app.route("/delete_article/<id>", methods=["GET", "POST"])
@login_required
def delete_article(id):
    mongo.db.articles.delete_one({"id": id})
    flash("Article deleted successsfully", "warning")
    return redirect(url_for("dashboard"))


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
                session["is_user_logged_in"] = True
                session["first_name"] = found_user["first_name"]
                session["last_name"] = found_user["last_name"]
                session["email"] = found_user["email"]
                flash("Login successfull", "success")
                return redirect("/dashboard")
            else:
                print("incorrect password")
                flash("Invalid password provided", "danger")

        else:
            print("no user found")
            flash("User not registered", "danger")

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

        flash("User registered successfull", "success")

        return redirect("/login")

    print("its an get call")
    return render_template("signup.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("Successfully logged out", "success")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.secret_key = "shfgdekh"
    app.run(debug=True, port=5001)
