import random

ascii_art = r"""
 _    _                                        
| |  | |                                       
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/                       
"""

stages = [
    r"""
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """
]

words = [
    "apple",
    "bicycle",
    "computer",
    "dolphin",
    "elephant",
    "festival",
    "giraffe",
    "harmony",
    "internet",
    "jungle",
    "kangaroo",
    "lighthouse",
    "mountain",
    "notebook",
    "ocean",
    "penguin",
    "quartz",
    "rainbow",
    "sunflower",
    "telescope",
    "umbrella",
    "vacation",
    "whisper",
    "xylophone",
    "yacht",
    "zebra",
    "balloon",
    "crystal",
    "dragonfly",
    "emerald"
]

gameOver = False
mistakes = 0
word = random.choices(words)[0]
attempts = []
print(ascii_art)


def currentWord():
    current = ""
    for char in word:
        if char in attempts:
            current += f"{char.upper()} "
        else:
            current += "_ "

    return current


while not gameOver:
    guess = input("What letter would you like to guess: ")
    if len(guess) != 1 or guess.isalpha() != True:
        print("Invalid input. Try Again!")
    else:
        if guess not in attempts:
            attempts.append(guess)
            if guess not in word:
                mistakes += 1
                print(f"The letter {guess} is not in the word.")
            else:
                print(f"You guessed correctly, the letter {guess} is in the word.")
        else:
            print("You have already guessed that letter. Try Another letter!")

        if mistakes == len(stages) - 1:
            gameOver = True
            print("You ran out of lives. You lose!")
            print(stages[mistakes])
            print(f"The word was: {word}")
        else:
            if word.lower() == currentWord().lower().replace(" ", ""):
                gameOver = True
                print(f"CONGRATULATION! YOU WON! THE WORD WAS: {word}")
            else:
                print(stages[mistakes])
                print(f"Your current guess: {currentWord()}")
