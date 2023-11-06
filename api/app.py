import re
import requests

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


@app.route("/get_username", methods=["GET"])
def get_username():
    return render_template("get_gitname.html")


@app.route("/get_username/result", methods=["POST"])
def submit_username():
    input_username = request.form.get("username")
    response = requests.get(
        f"https://api.github.com/users/{input_username}/repos"
    )
    if response.status_code == 200:
        repos = response.json()
        repos_data = []
        for repo in repos:
            commits_url = repo[]
        for data in repos:
            data_list = {
                'author' : data['commit']['author']['name'],
                'message' : data['commit']['message'],
                'time' : data['commit']['author']['date']
            }
            repos_list.append(data_list)
        return render_template(
            "username_hello.html",
            username=input_username,
            repositories=repos_list)
    else:
        error_message = (
            f"Error exist when getting the data from {input_username} repos"
        )
        return render_template(
            "username_hello.html",
            username=input_username,
            error=error_message)





@app.route("/get_username/result", methods=["POST"])
def submit_username():
    input_username = request.form.get("username")
    repos_response = requests.get(f"https://api.github.com/users/{input_username}/repos")
    if repos_response.status_code == 200:
        repos = repos_response.json()
        repos_data = []
        for repo in repos:
            commits_url = repo['commits_url'].split('{')[0]  # Remove the {/sha} part from the URL
            commits_response = requests.get(commits_url)
            if commits_response.status_code == 200:
                commits = commits_response.json()
                if commits:  # Check if there is at least one commit
                    latest_commit = commits[0]  # Get the latest commit
                    commit_data = {
                        'author': latest_commit['commit']['author']['name'],
                        'message': latest_commit['commit']['message'],
                        'date': latest_commit['commit']['author']['date']
                    }
                    repos_data.append(commit_data)
                else:
                    repos_data.append({'author': None, 'message': None, 'date': None})
        return render_template("username_hello.html", username=input_username, repositories=repos_data)
    else:
        error_message = f"Error fetching repositories for user {input_username}"
        return render_template("username_hello.html", username=input_username, error=error_message)
























@app.route("/query", methods=["GET"])
def query():
    input_query = request.args.get("q")
    return process_query(input_query)


def process_query(input_query):
    if input_query.startswith("What is your name"):
        return "superteam"

    if "dinosaurs" in input_query:
        return "Dinosaurs ruled the Earth 200 \
million years ago"

    if "asteroids" in input_query:
        return "Unknown"

    if input_query.startswith("Which of the following numbers is the largest"):
        result = find_largest_number(input_query)
        return result

    if "plus" in input_query:
        result = add_numbers(input_query)
        return result

    if "minus" in input_query:
        result = subtract_numbers(input_query)
        return result

    if "multiplied" in input_query:
        result = mul_numbers(input_query)
        return result

    if input_query.startswith("Which of the following numbers are primes"):
        result = find_primes(input_query)
        return result


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
    match = re.search(r'What is (\d+) minus (\d+)?', query)

    if match:
        A = int(match.group(1))
        B = int(match.group(2))

        result = A - B
        return str(result)
    else:
        return None


def add_numbers(query):
    match = re.search(r'What is (\d+) plus (\d+)?', query)

    if match:
        A = int(match.group(1))
        B = int(match.group(2))

        result = A + B
        return str(result)
    else:
        return None


def mul_numbers(query):
    match = re.search(r'What is (\d+) multiplied by (\d+)?', query)

    if match:
        A = int(match.group(1))
        B = int(match.group(2))

        result = A * B
        return str(result)
    else:
        return None


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def find_primes(query):
    match = re.search(r'Which of the following \
numbers are primes: (.+)?', query)
    if match:
        numbers_part = match.group(1)
        numbers = [int(num) for num in re.findall(r'\d+', numbers_part)]
        prime_numbers = [num for num in numbers if is_prime(num)]
        return str(prime_numbers)


if __name__ == '__main__':
    app.run(debug=True)
