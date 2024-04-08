from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html", name="User")

@views.route("/profile")
def profile():
    return render_template("profile.html")

@views.route("/Health")
def Health():
    return render_template("health.html")

@views.route("/article")
def article():
    return render_template("article.html")

@views.route("/json")
def get_json():
    return jsonify({'name': 'User', 'coolness': 10})


@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)


@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.get_json"))

@views.route("article/AI")
def go_to_AI():
    return render_template("AI.html")

@views.route("/Jinja")
def go_to_Jinja():
    return render_template("Jinja.html")