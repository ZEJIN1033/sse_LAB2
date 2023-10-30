# from app import process_query


# def test_knows_about_dinosaurs():
#     assert process_query("dinosaurs") == "Dinosaurs ruled the Earth 200 \
# million years ago"


# def test_does_not_know_about_asteroids():
#     assert process_query("asteroids") == "Unknown"


# def test_invalid_input():
#     assert process_query("abc") == "Invalid input"


# def test_team_name():
#     assert process_query("What is your name?") == "apex legend"


# def test_compare():
#     assert process_query("Which of the following numbers \
# is the largest:33,50,65?") == "65"


import app  # Import your Flask application
import pytest

@pytest.mark.parametrize("input_query, expected_result", [
    ("What is 5 plus 3?", 8),
    ("What is 10 plus 15?", 25),
    ("What is 100 plus 200?", 300) # Test an invalid query
])
def test_process_query(input_query, expected_result):
    result = app.process_query(input_query)
    assert result == expected_result

