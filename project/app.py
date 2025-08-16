from cs50 import SQL
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

db = SQL("sqlite:///informations.db")



@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    childhood = db.execute("SELECT description FROM informations WHERE name = ?", "Childhood")[0]["description"]
    highschool = db.execute("SELECT description FROM informations WHERE name = ?", "High School")[0]["description"]
    dreams = db.execute("SELECT description FROM informations WHERE name = ?", "Dreams")[0]["description"]
    now =db.execute("SELECT description FROM informations WHERE name = ?", "Present plans")[0]["description"]

    return render_template("about.html", childhood=childhood, highschool=highschool, dreams=dreams, now=now)


@app.route("/education")
def education():
    college =db.execute("SELECT description FROM informations WHERE name = ?", "College Education")[0]["description"]
    return render_template("education.html",college=college)

@app.route("/aerospace")
def aerospace():
    aerospace =db.execute("SELECT description FROM informations WHERE name = ?", "Aerospace field")[0]["description"]
    aero =db.execute("SELECT description FROM informations WHERE name = ?", "Aerodynamic")[0]["description"]
    structure =db.execute("SELECT description FROM informations WHERE name = ?", "Structure")[0]["description"]
    prop =db.execute("SELECT description FROM informations WHERE name = ?", "Propulsion")[0]["description"]
    cont =db.execute("SELECT description FROM informations WHERE name = ?", "Control")[0]["description"]
    space =db.execute("SELECT description FROM informations WHERE name = ?", "Space")[0]["description"]
    return render_template("aerospace.html",aerospace=aerospace, aero=aero, structure=structure, prop=prop, cont=cont, space=space)
