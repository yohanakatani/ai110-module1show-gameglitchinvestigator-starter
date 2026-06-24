from logic_utils import check_guess

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_hint_too_high_says_go_lower():
    # Bug fix: when guess > secret, message must say Go LOWER, not Go HIGHER
    outcome, message = check_guess(60, 50)
    assert "LOWER" in message

def test_hint_too_low_says_go_higher():
    # Bug fix: when guess < secret, message must say Go HIGHER, not Go LOWER
    outcome, message = check_guess(40, 50)
    assert "HIGHER" in message
