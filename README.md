# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Purpose:** A number guessing game where the player tries to guess a randomly generated secret number within a limited number of attempts. The game provides directional hints after each wrong guess and awards points based on how quickly the player wins.

**Bugs found:**
- Hint messages were reversed: "Go HIGHER" appeared when the guess was above the secret and "Go LOWER" when it was below.
- The "New Game" button reset attempts to 0, but the game initialized attempts at 1, causing an off-by-one inconsistency in the attempt counter display.
- The "Hard" difficulty returned range 1–50 while "Normal" returned 1–100, making Hard easier than Normal.

**Fixes applied:**
- Moved `check_guess` from `app.py` into `logic_utils.py` and corrected the swapped hint messages.
- Fixed the existing starter tests (they compared a tuple to a string) and added two new tests targeting the hint messages directly.

## 📸 Demo Walkthrough

1. Player opens the app and selects Normal difficulty (range 1–100, 8 attempts).
2. Player enters a guess of 30. The secret is 50. Game shows "Too Low — Go HIGHER" and deducts 5 points from score.
3. Player enters a guess of 70. Game shows "Too High — Go LOWER" and deducts 5 points from score.
4. Player enters a guess of 50. Game shows "🎉 Correct!" — balloons appear and the final score is displayed.
5. Player clicks "New Game" to reset and play again with a fresh secret number.

## 🧪 Test Results

```
============================= test session starts =============================
platform win32 -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0
collected 5 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 20%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 40%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 60%]
tests/test_game_logic.py::test_hint_too_high_says_go_lower PASSED        [ 80%]
tests/test_game_logic.py::test_hint_too_low_says_go_higher PASSED        [100%]

============================== 5 passed in 0.13s ==============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
