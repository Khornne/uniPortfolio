Password_Input = input("Choose a password: ")

if len(Password_Input) < 8:
    print("Password must be 8 characters minimum")
    exit(0)
elif len(Password_Input) > 12:
    print("Password must be 12 characters maximum")
    exit(0)
      
Password_Confirm = input("Re-enter password to confirm: ")


if Password_Input == Password_Confirm:
    print("Password set")
else:
    print("Error! Password does not match. Please try again")

