from flask import Flask, render_template, request
import re

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
    # match = re.match(r'What is (\d+) plus (\d+)\?', query)

    # if match:
    #     num1 = float(match.group(1))
    #     num2 = float(match.group(2))
    #     result = num1 + num2
    # else:
    #     result = "Invalid query format"  # Provide a default value for cases with no match

    # return result


    question, numbers = input_query.split(':')
    if question == "Which of the following numbers is the largest":
        return find_largest(input_query)
    else:
        return "Invalid input"

    # if input_query == "dinosaurs":
    #     return "Dinosaurs ruled the Earth 200 million years ago"
    # elif input_query == "asteroids":
    #     return "Unknown"
    # elif input_query == "What is your name?":
    #     return "apex legend"
    # else:
    #     return "Invalid input"
    

def find_largest(query):
    question, numbers =query.split(':')

    number = numbers.split('.')

    A = int(number[0].strip())
    B = int(number[1].strip())
    C = int(number[2].strip())

    largest = max(A,B,C)

    return largest