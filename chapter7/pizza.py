# Author: Holly Norton
# A program that prompts the user to enter a series of pizza toppings
# until they enter the word quit.  Then print the message to the user.

prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"  I'll add {topping} to your pizza.")
    else:
        break
