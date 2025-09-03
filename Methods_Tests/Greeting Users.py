# Greeting users using functions
user_name = input("What's your name: ")
def greet(user_name): #Function with argument (user_name is the argument)
    print("Good Day,", user_name)
greet(user_name)

#Or like this
def greet_friends(a, Thanks):
    print("Good Day,", a)
    print(Thanks)

greet_friends("Harry", "Thank you")
greet_friends("Rohan", "Thank you")
greet_friends("Shubham", "Thanks")
