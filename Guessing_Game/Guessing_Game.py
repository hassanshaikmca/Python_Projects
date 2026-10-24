import random

secret_number = random.randint(1, 10)

print("===== NUMBER GUESSING GAME =====")
print("I selected a number between 1 and 10.")
print(secret_number)

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low! Try a bigger number.")

    elif guess > secret_number:
        print("Too high! Try a smaller number.")

    else:
        print("Congratulations! You found the number:", secret_number)
        break

print("Game Over!")