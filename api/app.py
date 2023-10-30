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
    match = re.match(r'What is (\d+) plus (\d+)\?', input_query)

    if match:
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        result = num1 + num2
        return result

#     question, numbers = input_query.split(':')
#     if question.strip() == "Which of the following numbers is the largest":
#         return render_template("result.html", result=find_largest(numbers))
#     else:
#         return "Invalid input"

# def find_largest(numbers):
#     number_list = numbers.split('.')
#     number_list = [int(num.strip()) for num in number_list]

#     if len(number_list) > 0:
#         largest = max(number_list)
#         return largest
#     else:
#         return "No numbers provided"
