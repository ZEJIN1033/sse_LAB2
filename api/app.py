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
    if input_query.startswith("Which of the following numbers is the largest"):
        result = find_largest_number(input_query)
        return result
    
    if input_query.startswith("What is "):
        match = re.search(r'What is (\d+) plus (\d+)\?', input_query)

        if match:
            num1 = int(match.group(1))
            num2 = int(match.group(2))
            result = num1 + num2
            return result

    # result = subtract_numbers(input_query)
    # if result is not None:
    #     print(f"The result is: {result}")


    # match1 = re.match(r'What is (\d+) multiplied by (\d+)\?', input_query)

    # if match1:
    #     num1 = int(match.group(1))
    #     num2 = int(match.group(2))
    #     result = num1 * num2
    #     return result

    # if query.startswith("Which of the following numbers is the largest"):
    #     result = find_largest_number(query)
    #     return result
    

    # question, numbers = query.split(':')
    # if question.strip() == "Which of the following numbers is the largest":
    #     return render_template("result.html", result=find_largest(numbers))
    # else:
    #     return "Invalid input"


def find_largest_number(query):
    match = re.search(r'(\d+),\s*(\d+),\s*(\d+)', query)

    if match:
        A = int(match.group(1))
        B = int(match.group(2))
        C = int(match.group(3))
        
        largest = max(A, B, C)
        return str(largest)
    else:
        return "Invalid input"
    

def subtract_numbers(query):
    # 使用正则表达式匹配数字A和数字B
    match = re.search(r'What is (\d+) minus (\d+)', query)

    if match:
        A = int(match.group(1))
        B = int(match.group(2))

        # 计算A - B 的值
        result = A - B
        return str(result)
    else:
        return None
