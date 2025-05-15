import random

guess = random.randint(1, 5)

print("Welcome to the guessing game!")
print("I have selected a number between 1 and 5.")
print("Try to guess it!")

while True:
    user_input = input("Enter your guess (or 'exit' to quit): ")

    if user_input.lower() == 'exit':
        print("Thanks for playing!")
        break

    try:
        guess_number = int(user_input)
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess_number < 1 or guess_number > 5:
        print("Your guess is out of range. Please try again.")
        continue

    if guess_number == guess:
        print("Congratulations! You guessed the right number.")
        break
    else:
        print("Wrong guess. Try again!")
