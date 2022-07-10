import enchant
from colorama import Fore, init

# Initialise colorama and enchant
init(autoreset=True)
e = enchant.Dict("en_US")

# Checks if the word is valid i.e a real word and 5 letters long
def isvalid(word):
    if len(word) == 5:
        if e.check(word):
            return True
        return False
    return False

# checks if user has won the game
def wordle(word, guess):
    return word == guess

# returns a list containing the letters that are in the word but not in correct positions
def correct_letters(word, guess):
    letters = []
    for i in word:
        if i in guess and i not in letters and word.count(i) == 1:
            letters.append(i)
        elif i in guess and word.count(i) > 1:
            if guess.count(i) != letters.count(i):
                letters.append(i)
    return letters

# returns a list containing the letters that are in the word in correct positions
def correct_positions(word, guess):
    positions = {}
    for i in range(len(word)):
        if word[i] == guess[i]:
            positions[i] = word[i]
    return positions

# prints the wordle
def print_word(guess, word, correct_letters, correct_positions):
    for i in range(len(guess)):
        if guess[i] in correct_letters and guess[i] not in correct_positions.values():
            print(Fore.YELLOW + guess[i], end="")
            try:
                correct_letters.remove(guess[i])
            except:
                print("testing")
        elif guess[i] in correct_positions.values():
            try:
                if guess[i] == correct_positions[i]:
                    print(Fore.GREEN + guess[i], end="")
            except:
                print(Fore.RED + guess[i], end="")
        else:
            print(Fore.RED + guess[i], end="")
    print()

#function to give hints
def give_hint(word, correct_positions):
    try:
        position = int(input("Enter the position of the letter you would like to uncover: "))
    except:
        print("Something went wrong, try again later.")
        return
    if position-1 in correct_positions:
        print("\n" + Fore.GREEN + "You have already uncovered this letter. Use your hint wisely.\n")
    else:
        print("\n" + Fore.YELLOW + "The letter in that position is " + word[position-1] + "\n")
        return True