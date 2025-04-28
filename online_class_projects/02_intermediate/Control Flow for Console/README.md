
<h1 align="center">🎮 High-Low Game – Python</h1>
<h3 align="center">A simple command-line guessing game using Python</h3>


---

## 📜 Code Explanation

This is a step-by-step explanation of how the game works:

---

### 🌟 What is this code?

This is a simple Python game called **"High-Low Game"**. You’ll be shown a number (your number), and you have to guess if your number is **higher** or **lower** than the computer’s secret number.

---

### 📦 Constants and Setup

```python
NUM_ROUNDS = 5  # Number of rounds to play
```

- The game will be played for 5 rounds.

---

### 🎯 Function: `get_valid_choice()`

```python
def get_valid_choice():
    while True:
        choice = input("Do you think your number is higher or lower than the computer's?: ").lower()
        if choice in ['higher', 'lower']:
            return choice
        print("Please enter either higher or lower: ", end="")
```

- Asks the player to input "higher" or "lower".
- Repeats until the input is valid.

---

### 🎮 Function: `play_game()`

```python
def play_game():
    score = 0
```

- Initializes your score to 0.

```python
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
```

- Prints a welcome message.

---

### 🔁 Loop Over Rounds

```python
    for round_num in range(1, NUM_ROUNDS + 1):
```

- Plays the game for 5 rounds.

---

### 🧮 Each Round Process

```python
        player_num = random.randint(1, 100)
        computer_num = random.randint(1, 100)
```

- Generates two random numbers (1–100):
  - One for the player (shown).
  - One for the computer (hidden initially).

```python
        print(f"Your number is {player_num}")
```

- Displays the player's number.

```python
        player_choice = get_valid_choice()
```

- Asks if your number is higher or lower than the computer's.

---

### 🏆 Check If Player Won

```python
        player_won = False
        if player_choice == 'higher' and player_num > computer_num:
            player_won = True
        elif player_choice == 'lower' and player_num < computer_num:
            player_won = True
```

- Compares your choice and the numbers to decide if you won the round.

---

### ✅ Update Score & Show Result

```python
        if player_won:
            score += 1
            print(f"You were right! The computer's number was {computer_num}")
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_num}")

        print(f"Your score is now {score}")
```

- Updates your score and shows the computer’s number.

---

### 🏁 Game Over – Final Message

```python
    print("\nThanks for playing!")
    if score == NUM_ROUNDS:
        print("\nWow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("\nGood job, you played really well!")
    else:
        print("\nBetter luck next time!")
```

- Prints a final message depending on how well you did.

---

### 🧠 Final Part (Start Game)

```python
if __name__ == "__main__":
    play_game()
```

- Runs the game when the script is executed directly.

---

## 📝 Summary

- You play 5 rounds.
- Each round shows you a number.
- You guess whether your number is **higher** or **lower** than the computer's.
- You earn points for correct guesses.
- Your total score and performance message is shown at the end.

---
