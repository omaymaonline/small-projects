# ASCII Art
phase0 = """
  +---+
  |   |
      |
      |
      |
      |
=========

"""
phase1 = """
  +---+
  |   |
  O   |
      |
      |
      |
=========

"""
phase2 = """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========

"""
phase3 = """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========

"""
phase4 = """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

"""
phase5 = """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========

"""
phase6 = """
   !!!Game Over!!!

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========

"""

hangman_phases = [phase0, phase1, phase2, phase3, phase4, phase5, phase6]

# Welcome
print("Welcome to Hangman Game!")

# Create the word and the field
word = ["b", "i", "c", "y", "c", "l", "e"]
field = ["_" for _ in word]
print(f"{' '.join(field)}\nYou need to guess the word, it's composed of {len(word)} letters.")

# Chances
chance = 6
errors = 0
print(f"You have {chance} lives.\nGet ready!")

trials=[]
# Game loop
while errors < chance:
    letter = input("Enter a letter: ").lower()
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter and field[i] == "_":
                field[i] = letter
                break

        print(' '.join(field))
    else:
        if letter in trials:
            print("You already tried that letter.")
            continue
        errors += 1
        print("Wrong guess!")
        print(hangman_phases[errors])
        print(f"Lives left: {chance - errors}")
        trials.append(letter)

    if "_" not in field:
        print("🎉 You won!")
        break
else:
    print("💀 Game over! The word was:", ''.join(word))