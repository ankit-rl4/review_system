from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

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

    def __init_(self, rating, review_str):
        self.rating = rating
        self.review_str = review_str


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == "POST":
        Review = request.form["text"]
        dreview = review(rating=0, review_str=Review)
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
