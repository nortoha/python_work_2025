favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\n")

# list of people
coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']

# loop through list and print messages
for coder in coders:
    if coder in favorite_languages.keys():
        print(f"Thank you for taking the poll, {coder.title()}!")
    else:
        #print(f"{coder.title()}, what's your favorite programming language?")
        fav = input(f"{coder.title()}, what's your favorite programming language?")
        favorite_languages[coder] = fav

# reprint the list and see our new friends
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
