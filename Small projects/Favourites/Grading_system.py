#Setting up variables
user_name = input("Enter your full name: ")
total = input("Do you want to see have you passed overall or not (y/n): ").lower()

#If-elif-else ladder
if total == "n":
    subject = input("Which subject do you want to see?: ")
    subject_marks = int(input("Great! Enter your marks : "))
    if subject_marks >= 90:
        print(f"Hooray {user_name}! you passed, atleast in this subject, unfortunately I don't have a cookie :(")
    elif subject_marks < 90:
        print(f"YOU FAILED {user_name}!!! atleast in this subject :)")

elif total == "y":
    marks = int(input("Sure! then tell your total marks: "))
    if marks >= 90:
        print(f"Hooray! you passed THE CLASS {user_name}, unfortunately I don't have a cookie :(")
    elif marks < 90:
        print(f"YOU FAILED {user_name}!!! The class :(")

else:
    print("You had one job, that is to type y or n, you clearly failed in nursery")
    print("FAILURE and a half!!")
    print("Sorry buddy, you can try later don't feel bad, we all make mistakes")

