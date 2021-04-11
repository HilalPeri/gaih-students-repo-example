#Day 3
 #User login Application
username = "HilalPeri"
password = "GlobalAIHub_2021"

username0 = input("Please enter your username:")
password0 = input("Please enter your  password:")

if (username0 != username and password0 != password):
    print("Your username and password is incorrect.")
elif (username0 == username and password0 != password):
    print("Your password is incorrect.")
elif (username0 != username and password0 == password):
    print("Your username is incorrect.")
else:
    print("Congratulations, you have succesfully logged in.")
