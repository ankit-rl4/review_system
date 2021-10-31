from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.static_folder = 'static'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ankit.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
flag = 0


class review(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    review_str = db.Column(db.String(300))
    time = db.Column(db.String(300))

    def __init_(self, rating, review_str, time):
        self.rating = rating
        self.review_str = review_str
        self.time = time


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == "POST":

        Review = request.form["text"]
        try:
            rating = request.form.getlist("rate")
        except:
            return render_template("index.html", data=True)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        rating = int(rating[0])
        dreview = review(rating=rating, review_str=Review, time=dt_string)
        db.session.add(dreview)
        db.session.commit()

        return render_template("ind.html")
    return render_template("index.html")


@app.route("/admin", methods=['GET', 'POST'])
def admin():
    return render_template("adminlogin.html")


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    if request.method == "POST":
        user = request.form["user"]
        passw = request.form["pass"]
        if user == 'admin' and passw == 'admin':
            global flag
            flag = 1
            return redirect(url_for("review_list"))
        else:
            return render_template('adminlogin.html')
    return render_template("adminlogin.html")


@app.route("/review_list", methods=['GET', 'POST'])
def review_list():
    if flag == 1:
        review_data = review.query.all()
        return render_template("review_list.html", data=review_data)
    else:
        return render_template("adminlogin.html")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
