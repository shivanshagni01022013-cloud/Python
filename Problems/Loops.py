#Table of 5
n = int(input("Enter your number: "))
for i in range(1, 11):
    product = (f"{n} X {i} = {n * i}")
    print(product)
else:
    print("Done using for loop")

#Using while loop
n = int(input("Enter your number: "))
i = 1
while(i<=10):
    print(f"{i} X {n}: {i*n}")
    i+= 1
else:
    print("Done using while loop")

#Number is prime or not
num = int(input("Enter your number: "))

if num < 2:
    print("This number is not prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("This number is not prime")
            break
    else:
        print("This number is prime")


      

