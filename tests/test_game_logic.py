from logic_utils import check_guess, get_range_for_difficulty

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

def test_hard_range_wider_than_normal():
    # Bug fix: Hard was 1-50 (narrower than Normal's 1-100) — now Hard must be wider
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high

def test_single_digit_guess_against_two_digit_secret():
    # Bug fix: str coercion caused "6" > "50" == True, returning "Too High" wrongly
    # With int comparison, guess=6 < secret=50 must return "Too Low"
    outcome, message = check_guess(6, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
