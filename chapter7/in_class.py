import random

my_num = random.randint(1, 10)

guess = input("Guess a number between 1 and 10: ")
while guess != 'quit':
    if my_num==int(guess):
        print(f"Congratulations you guess the number. It was {guess}")
        break
    else:
        print("Incorrect guess again.")
        guess = input("Guess a number between 1 and 10: ")

#index = 10
#while  0 <= index <= 10:
#    print(random.randint(1, 100))
#    # decrement the counter
#    index -= 1