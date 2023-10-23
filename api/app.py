from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    return render_template("hello.html", name=input_name, age=input_age)


@app.route("/query", methods=["GET"])
def query():
    input_query = request.args.get("q")
    process_query(input_query)


def process_query(input_query):

    if input_query == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    elif input_query == "asteroids":
        return "Unknown"
    else:
        return "Invalid input"
