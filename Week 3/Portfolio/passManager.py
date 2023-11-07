Password_Input = input("Choose a password: ")
Password_Confirm = input("Re-enter password to confirm: ")

if Password_Input == Password_Confirm:
    print("Password set")
else:
    print("Error! Password does not match.")


