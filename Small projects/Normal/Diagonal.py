#Diagonal of a rectangle
import math

length = int(input("Enter the length of a rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))
diagonal = math.sqrt(length**2 + breadth**2)

print("Diagonal is: ", round(diagonal, 2))