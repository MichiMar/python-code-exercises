import random

def high_low_game():
    guesses_taken = 0
    min_num = 0 
    max_num = 100

    print("Welcome to 'High-Low Game'. What is your name?")
    username = input()

    number = random.randint(min_num, max_num)
    print(f"Ok {username}, I'm thinking in a number between {str(min_num)} and {str(max_num)}, and you have 10 attemps")

    def guess_try():
        pass

    while True:
        while guesses_taken < 10:
            print("Can you guses wich one is?\n")
            guess = input()
            guess = int(guess)

            guesses_taken += 1

            if guess < number:
                print("Incorrect, try again with a higher number\n")
            elif guess > number:
                print("Incorrect, try again with a lower number\n")
            elif guess == number:
                break

        def play_again():
            print("do you want to play again?")
            answer = input("'Y': Yes, 'N': No")
            if answer == 'Y' :
                high_low_game()
            elif answer == 'N' :
                print("Ok, come back soon and let's play again. See Ya !!")
                return False
            else:
                print("That choice is not in the choice list")

        if guess == number:
            print(f"Correct!! Congratulations {username}, you won this game in {str(guesses_taken)} attemps!!")
            play_again()
        else:
            print(f"To bad {username}, you miss this round, I was thinking in {number}")
            play_again()
    
    high_low_game()
