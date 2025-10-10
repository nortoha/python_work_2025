
#message = input("What is your favorite ice cream flavor? ")
#print(message)

#fav_num = input("What is your favorite number? ")
#print(int(fav_num)+10)

age = 13
if age in range(13,20):
    print("You are a teenager 1.")

if age>=13 and age<=19:
    print("You are a teenager 2.")

favorite_numbers = {
    'alice': [7, 42],
    'bob': [13],
    'carol': [3, 9, 27]
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are: {', '.join(str(num) for num in numbers)}")


random_quote = 'Benjamin Franklin once said'
print(random_quote + ', "Time is money"') 