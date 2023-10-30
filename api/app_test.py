from app import process_query


def test_knows_about_dinosaurs():
    assert process_query("dinosaurs") == "Dinosaurs ruled the Earth 200 \
million years ago"


def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"


def test_invalid_input():
    assert process_query("abc") == "Invalid input"


def test_team_name():
    assert process_query("What is your name?") == "apex legend"


def test_add():
    assert process_query("What is 45 plus 45?") == "90"


def test_compare():
    assert process_query("Which of the following numbers \
is the largest:33,50,65?") == "65"
