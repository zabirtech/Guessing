rules = print("Welcome to the word guessing game! You only have three guesses to guess the right word! ")
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
secret_word_hint = "You guessed wrong here is a hint: Animal with a long neck"


while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1



    else:

        out_of_guesses = True







if out_of_guesses and secret_word_hint:
    print("you are out of guess you lose")
    print(secret_word_hint)
else:
    print("You win")