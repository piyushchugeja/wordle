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
print("5. The hints will be given as colours, they signify the following:\n")
print(Fore.GREEN + "   - Green: Correct letter in correct position\n")
print(Fore.YELLOW + "   - Yellow: Correct letter in wrong position\n")
print(Fore.RED + "   - Red: Incorrect letter\n")
print("6. You can ask for a hint by entering 'hint'.\n")
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
        if guess != "hint":
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
        else:
            if tries == 0:
                print("You cannot use hints on your first try.\n")
            elif taken_hint:
                print("\n" + Fore.RED + "You have already used your hint :(\n")
            else:
                taken_hint = give_hint(word, correct_positions(word, previous_guess))
    if not hasWon:
        words.print_losing_message(word)
    if input("Do you want to play again? (y/n) ") == "y":
        wantsToPlay = True
    else:
        exit()