def last_character_removal(rem_character):
    if len(rem_character) <= 1:
        return rem_character
    else:
        return rem_character[:-1]
    

character = input("Please enter a string: ")

results = last_character_removal(character)

print(results)