"""

Guess a secret number in maximum 3 chances.
Using While-else

"""

print("Guess a number between 0-9, You get 3 chances only...")
secret_number = 9
guess_limit = 3
guess_count = 0

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!!")
        break
else:
    print("Game Over!!")
