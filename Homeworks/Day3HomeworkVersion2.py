username = "HilalPeri"
password = "GlobalAIHub_2021"
check = True

for x in range(5):
    username0 = input("Please enter your username:")
    password0 = input("Please enter your  password:")
    if (username0 == username and password0 == password):
        print("Congratulations, you have succesfully logged in.")
        check = False
        break
    elif (username0 == username and password0 != password):
        print("Your password is incorrect. Please try again.")
        x=x+1
    elif (username0 != username and password0 == password):
        print("Your username is incorrect. Please try again.")
        x=x+1
    else:
        print("Your username and password is incorrect. Please try again.")
        x=x+1
if x not in range(5):
    print("You have made 5 incorrect entries. Your account has been blocked.")