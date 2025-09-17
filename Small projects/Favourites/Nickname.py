# Take your name and your best friend’s name and print a nickname by combining parts of both names.Take your name and your best friend’s name and print a nickname by combining parts of both names.
import random

list = []
name1 = input("Enter your name: ")
name2 = input("Enter your friend's name: ")
name3 = input("Enter your friend's name again: ")
name4 = input("Enter your friend's name for the last time: ")

list.append(name1)
list.append(name2)
list.append(name3)
list.append(name4)

print(f"The nickname I have created is: {random.choice(list)} {random.choice(list)}")