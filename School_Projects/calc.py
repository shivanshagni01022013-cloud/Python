#Setting up variables
n1 = float(input("Enter your first number: "))
n2 = float(input("Enter your second number: "))

#Setting up operating variables
add = n1+n2
sub = n1-n2
mul = n1*n2
div = n1/n2

#Actually printing the result
print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Divison: {round(div, 2)}")

#Round-function syntax => round(*variable*, *To what place you want to round it*=> say 2)