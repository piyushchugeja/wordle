import words
from wordle import *

# main function
wantsToPlay = True
print("\n***********************************")
print("\n   Welcome to the wordle game!")
print("\n***********************************\n")

print("1. You will be given a word and you have to guess it.\n")
print("2. Only valid English language words with only 5 letters are accepted. Else the word will be termed as invalid.\n")
print("3. You will get 6 tries in all.\n")
print("4. You will be given hints on letters are in which positions.\n")
print("***********************************\n")
choice = input("Press enter to start the game or type 'exit' to exit: ")
if choice == "exit":
    exit()

while wantsToPlay:
    hasWon = False
    word = words.get_word()
    tries = 0
    taken_hint = False
    while not hasWon and tries < 6:
        print("Try",tries+1)
        guess = input("Enter your guess: ")
        if isvalid(guess):
            if wordle(word, guess):
                words.print_winning_message()
                hasWon = True
            else:
                tries += 1
                print_word(guess, word, correct_letters(word, guess), correct_positions(word, guess))
        else:
            print("Invalid word")
        previous_guess = guess
        print()
    if not hasWon:
        words.print_losing_message(word)
    if input("Do you want to play again? (y/n) ") == "y":
        wantsToPlay = True
    else:
        exit()