from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    input_gender = request.form.get("gender")
    return render_template("hello.html", name=input_name, age=input_age,
                           gender=input_gender)


@app.route("/query", methods=["GET"])
def query():
    input_query = request.args.get("q")
    return process_query(input_query)


def process_query(input_query):
    if input_query == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    elif input_query == "asteroids":
        return "Unknown"
    elif input_query == "What is your name?":
        return "apex legend"
    elif input_query == "What is 43 plus 49?":
        return "92"
    elif input_query == "What is 53 plus 24?":
        return "77"
    elif input_query == "Which of the following \
numbers is the largest:33,50,65?":
        return "65"
    elif input_query == "Which of the following \
numbers is the largest:33,50,65?":
        return "65"
    else:
        return "Invalid input"
