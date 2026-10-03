from logic_utils import check_guess

#FIX: Using AI I updated the testing code to unpack the tuple then compare the outomce with the string
#prevously it was direclty comparing the tuple to the string, which made the tests fail

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

#FIX: Used AI to add tests to make sure too-high/too-low hints were working correctly
def test_guess_too_low_secret_60():
    # If secret is 60 and guess is 50, it should be "Too Low"
    outcome, _ = check_guess(50, 60)
    assert outcome == "Too Low"

def test_guess_too_high_secret_60():
    # If secret is 60 and guess is 70, it should be "Too High"
    outcome, _ = check_guess(70, 60)
    assert outcome == "Too High"

def test_guess_too_low_by_one():
    # Off-by-one check: guess one below the secret is still "Too Low"
    outcome, _ = check_guess(59, 60)
    assert outcome == "Too Low"

def test_guess_too_high_by_one():
    # Off-by-one check: guess one above the secret is still "Too High"
    outcome, _ = check_guess(61, 60)
    assert outcome == "Too High"

def test_check_guess_accepts_string_secret():
    # check_guess is called with a stringified secret on even attempts in app.py,
    # so it must coerce secret to int before comparing
    outcome, _ = check_guess(50, "60")
    assert outcome == "Too Low"
