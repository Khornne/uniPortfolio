def displayTwice(msg):
    """Displays inputted message twice."""
    print(msg)
    print(msg)

message = input("Write a message: ")

results = displayTwice(message)

print(message)

# Task to display help
help(displayTwice)
