#Strings and methods

name = "harry"
my_name = "shivansh"

print(name[0:3]) 
print(name[-5:-1])
print(name.capitalize())
print(name.find("y"))
print(name.startswith("har"))
print(name.startswith("Har"))
print(name.endswith("rry"))
print(name.endswith("Rry"))
print(name.find("har"))
print(my_name.count("s"))

#Lists and methods

l1 = [7,9,"harry","Rohan",58,"Ankita", 34.434342123]
print(l1[0:4])
l1.remove("harry")
print(l1)
l1.append("Shivansh")
print(l1)
l1.insert(3,5)
print(l1)

'''NOTE: l1.sort()  (l1 is a list with multiple datatype)
         print(l1) - Will give an error as python can't sort multiple data types'''

l2 = [6, 8, 345, 2, 42342, 45039]
l2.sort()
print(l2) #Correct syntax
l2.remove(42342)
print(l2)

'''l2.pop(5)
   print(l2) - NOTE: It will give an error since lists are mutable
(as after removing 42342 from the list, the list changed leaving only 4 elements)'''

l2.pop(2)
print(l2) #Correct syntax as the index 2 is in range
l2.reverse()
print(l2)

#Tuples and methods

tup_1 = (4, "harry", "Pinku", 234.32, "Shivansh", "Tejas", 4)
print(tup_1)
print(tup_1.index("Pinku"))
print(tup_1.count(4))
#tuple slicing
tup_2 = (3, 5, 234, 242, 1, 433)
print(tup_2[1:4])
print(tup_2[-4:-1])
print(tup_2[0:4])

#Dictionary and methods

d = {} #Empty dictionary
marks_100 = {
    "Shivansh":100,
    "Tejas":69,
    "Atif":-777,
    "Markslist":[20, 12, 100, 323]
}
print(type(marks_100))
print(marks_100)
print(marks_100.get("Atif"))
print(marks_100.pop("Markslist"))
print(marks_100.keys())
print(marks_100.items())
marks_100.update({"Tejas":70, "Rohit":99})
print(marks_100)

#Sets and methods
#Sets are a collection of non-repetitive elements

set_1 = set() #Empty set
set_2 = {5, 4, 3, 3, 8, 9}
set_3 = {5, 4, 2, 7, 8, 10, 34}
set_4 = {4, 6, 7, 10, 45}
print(set_2) #Won't show duplicated items (Will show three only once)
print(len(set_3))
set_2.remove(4)
print(set_2)
item = set_3.pop()
print(item)
print(set_3)
print(set_2.pop())
print(set_2)
set_4.clear()
print(set_4)


