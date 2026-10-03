# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The hints were not accurate for the secret number. And the enter button didnt do anything. The new game button doesn't start a new game
**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| guess of 10 | "Go higher" | "Go Lower"      | app.py, check_guess |
| pressed "Enter" button | Decrease attempts| Did nothing | app.py, lines 147-188 |
| pressed "New game" | Start a new game | Did nothing | app.py, lines 140-145 |

---

## 2. How did you use AI as a teammate?

I used Claude. 
When I was asking it to help me fix the bug for too low/too high hints. It also gave me advice to fix comparisons between an int and string, which was causing some of the errors. I looked into the lines that the AI gave me and noticed this bug. So I decided to take the advice, which added a simple check to make sure comparison is between ints only.

When I was asking why pressing "New Game" is not actually starting a New Game it found the bug and presented it. It also gave some other issues, like how the code was regenerating the secret with hardcoded random.randint(1, 100) instead of using the difficulty-based low, high range. At this point I was focused on just getting the New Game to work and didn't want to deal with any other unrelated changes that might make me confused so I disregarded this issue, opting to fix the main one and then look into this later.


---

## 3. Debugging and testing your fixes

I added a number of tests, especially testing if the hints given were correct, in the test_game_logic.py. 
They were successful.
And I manually ran the game and played it to make sure the bugs like "New game" button were working and the hints were correct.

I also used AI to help me understand how some of the tests worked.


---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  Basically in a Streamlit app, when you intereact with anything the entire screen updates, so it runs the Python script again from top to bottom, called a rerun. So Anytime the user interacts with anything, it reruns the script.

  Session state is a dictionary that doesnt change across reruns for a user's session. So it would be used for remembering the secret number the entire user's session.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

  Make sure to read and understand what the AI is suggesting to change or take away
  Use source control to check the differences in the code
  Before asking AI to fix things, ask why the bug is happening. Basically try to understand the reasoning behind why something is wrong, instead of just blindly using AI to fix it for you.

- What is one thing you would do differently next time you work with AI on a coding task?

  I would do a bit of research or ask AI to explain streamlit to me because I have never used it before and it had some constraints that I didn't quite understand.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

  I used to think it was kind of something you blindly use and not have to think about as much
  But I realized its important to understand what the AI is doing and even ask questions, especially if later you have to update the code or fix bugs caused by AI.