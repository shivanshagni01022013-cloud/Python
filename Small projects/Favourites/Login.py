username = input("Enter your username: ")
password = input("Enter your password: ")
actual_username = "Shivansh"
actual_password = "jaijagat1feb2013"

if username == actual_username and password == actual_password:
    print(f"Welcome {actual_username}, Good to see you!")
else:
    print("Sorry, you may have either typed incorrect password or username, maybe both!")