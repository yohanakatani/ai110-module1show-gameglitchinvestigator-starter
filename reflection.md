# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game wasn't sharply responsive and the hints immediately seemed off — guessing a number lower than the secret told me to go lower, which was the opposite of what I expected.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  - The hints were reversed: "Go HIGHER" appeared when my guess was already above the secret number.
  - Clicking "New Game" did not properly reset the attempt counter, so the attempt display was inconsistent from the start.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guessed 60, secret was 50 | Hint should say "Go LOWER" since my guess is above the secret | Hint said "Go HIGHER" — the opposite direction | No error; wrong hint message displayed |
| Clicked "New Game" button | Game resets cleanly with full attempts available | Attempts reset to 0 via New Game but initialize to 1 on first load, so the display is off by one from the start | No error; attempt count is inconsistent |
| Selected "Hard" difficulty | Hard should be more challenging than Normal with a larger number pool | Hard returns range 1–50 while Normal returns 1–100, making Hard actually easier | No error; wrong range returned for Hard |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude Code to investigate the bugs in the game before applying any fixes. I described the symptoms I observed and shared the code files, then asked Claude to explain the logic step-by-step and pinpoint the flaws.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Claude correctly identified that the hint messages in `check_guess` were swapped — it pointed out that when `guess > secret` the code returns "Go HIGHER" instead of "Go LOWER." I verified this by manually testing the game: guessing 60 when the secret was 50 produced the wrong hint exactly as Claude described.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Claude initially surfaced five bugs, but I only needed three for this reflection. One of the extra bugs (the score formula off-by-one) was valid but not something I could reproduce by simply playing the game — it required reading the code closely, which made it harder to verify manually without running targeted tests.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was fixed when both the automated test passed and the live game behaved correctly. For the hint reversal, I ran `pytest tests/ -v` and confirmed all five tests passed, then verified manually by entering 60 against a secret of 50 and seeing "Go LOWER" instead of "Go HIGHER."

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
I ran `pytest tests/ -v` after the fix and all five tests passed, including `test_hint_too_high_says_go_lower` and `test_hint_too_low_says_go_higher`. These two new tests were the key ones — they would have caught the original bug immediately if they had existed before. The existing three starter tests also revealed a secondary issue: they were asserting against a bare string, but `check_guess` returns a tuple, so they would have failed even on correct code. Fixing those tests sharpened my understanding of the function's return shape.

- Did AI help you design or understand any tests? How?
Yes. Claude flagged that the existing starter tests were broken (comparing a tuple to a string) and suggested unpacking the return value. It also proposed the two new message-specific tests — checking for "LOWER" and "HIGHER" in the message string — which directly target the symptom described in the bug report rather than just the outcome label.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Every time you interact with a Streamlit app — clicking a button, typing in a box — the entire Python script reruns from top to bottom. That means any normal variable gets reset to its default value on every interaction. `st.session_state` is a dictionary that survives across these reruns, so anything you need to persist (like the secret number or attempt count) must be stored there. Think of it like a whiteboard that gets erased every second: `session_state` is the sticky note you put on the side so your important values survive the erase. In this project the secret number was stored in `st.session_state.secret` on first load and never overwritten during normal play, which is why it stayed consistent across guesses.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
I want to keep the habit of asking AI to explain code logic step-by-step before touching anything. Having Claude trace the execution path for me — without modifying any code first — gave me a clear mental model of the bug before I made a single change. That separation of "understand first, fix second" prevented me from chasing the wrong line.

- What is one thing you would do differently next time you work with AI on a coding task?
I would add the FIXME markers to the file myself before asking AI for the fix, instead of relying on the AI to place them. The assignment asked me to mark the "crime scene" manually, which is good practice because it forces me to commit to a hypothesis before delegating the repair. I let the AI mark and fix in one step, which skipped that verification moment.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
AI-generated code can look completely plausible — correct structure, no syntax errors, sensible variable names — while containing a logic inversion that only surfaces at runtime. This project taught me to treat AI output as a first draft that needs a human execution trace, not a finished product.
