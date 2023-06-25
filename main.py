import random

print("Welcome to the Number Guessing Game!")
numbers = [x for x in range(1, 101)]
random_number = random.choice(numbers)
print("I am thinking of a number between 1 and 100")

level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


def play_game(attempts):
    while attempts > 0:
        attempt = int(input("Make a guess: "))

        if attempt == random_number:
            print("Congratulations! You guessed the number. You win!")
            return

        elif attempt > random_number:
            print("Too high!")
        elif attempt < random_number:
            print("Too low!")

        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} attempts remaining.")
        else:
            print("Out of attempts. You lose.")


def final_game():
    if level == "easy":
        play_game(6)
    elif level == "hard":
        play_game(3)
    else:
        print("Invalid difficulty level. Please choose 'easy' or 'hard'.")


final_game()
