favorite_numbers = {
    'holly': [4, 17],
    'caroline': [19, 14, 21],
    'gus': [7, 12],
    }

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} likes the following numbers:")
    for number in numbers:
        print(f"  {number}")
