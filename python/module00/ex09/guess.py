from random import randint




def guess():
    print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!
""")
    secret_number = randint(1, 99)
    attempts = 0
    print(secret_number)
    while True:
        attempts += 1
        print("What's your guess between 1 and 99?")
        user = input(">> ")
        if user == "exit":
            print("Goodbye!")
            break
        elif int(user) > secret_number:
            print("Too high!")
        elif int(user) < secret_number:
            print("Too low!")
        else:
            print(f"Congratulations, you've got it!\nYou won in {attempts} attempts!")
            break


if __name__ == '__main__':
    guess()