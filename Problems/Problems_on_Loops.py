#Greeting people whose name start with "S"
l = ["Harry", "Soham", "Sachin Tendulkar", "Rahul"]

for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")

#Sum of first ten natural numbers

i = 1
n = int(input("Enter your number: "))
sum = 0

while(i<=n):
    sum += i
    i += 1
print(sum)

#Factorial

num = int(input("Enter your number: "))
factorial = 1
for f in range(1, num+1):
    factorial = f*factorial
print(f"The factorial of your number is: {factorial}")

    
    
