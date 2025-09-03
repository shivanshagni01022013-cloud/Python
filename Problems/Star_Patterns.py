#For n = 3
'''  *
    ***
   *****'''

n = int(input("Enter your number for star pattern: "))
for i in range(1, n+1):
    print(" "* (n-i), end = "")
    print("*"* (2*i-1), end = "")
    print("")
print("This is a full triangle")

''' *
    **
    **** '''

for i in range(1, n+1):
    print("*"* i, end = "")
    print("")
print("This is a half-triangle")  

'''***
   * *
   ***'''

for i in range(1, n+1):
    if(i == 1 or i == n):
        print("*"* n, end = "")
    else:
        print("*", end = "")
        print(" "*(n-2), end= "")
        print("*", end = "")
    print("")
print("This is a rectangle")


