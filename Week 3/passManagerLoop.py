BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber'] 


while True:
    Password_Input = input("Choose a password: ") 

    if len(Password_Input) > 8:
        print("Password must have a minimum of 8 characters")
        break
    elif len(Password_Input) > 12:
        print("Password must have a maximum of 12 characters")
        break
    elif Password_Input in BAD_PASSWORDS:
        print("Please choose a stronger password")
        break
    else:



    


Password_Confirm = input("Re-enter password to confirm: ")
if Password_Input == Password_Confirm:
    print("Password set")
    exit(0)

else:
    print("Error! Password does not match. Please try again.")

    

