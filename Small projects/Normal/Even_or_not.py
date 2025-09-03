#Program to check 2 number's sum is even or not

number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))
sum = number1+number2

if sum%2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")