def character_numbers(num_str):
    capital_character = 0
    lower_character = 0

    for char in num_str:
        if char.isupper():
            capital_character += 1
        elif char.islower():
            lower_character += 1

    return capital_character, lower_character

numbers = input("Please write a word: ")

captial_character, lower_character = character_numbers(numbers)

print(f"Captial Characters: {captial_character}")
print(f"Smaller Characters: {lower_character}")
            
