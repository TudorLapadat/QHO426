#Declare an empty list
bleh = []
meh = list()
#declare a non-empty list
yummy = ["Pizza", "Sarmale", "Ice Cream", "Carnati"]
#Print entire list
print(yummy)
#Print a single item 
print(yummy[2])
#print some items
print(yummy[:2])
#Add elements to our list (expand it) - addint at the end of the list
print(bleh)
bleh.append("Pierogi")
bleh.append("Steak")
bleh.append("Liver")
bleh.append("Horse meat")
print(bleh)
#Add multiple items to a list 
for i in range (2):
  bleh.append("salad")
print(bleh)
bleh.extend(["Racitura", "soup", "cat"])
print(bleh)
#insert items at specific positions on the list
bleh.insert(1, "Cabbage")
print(bleh)
bleh.insert(4, "Mushed peas")
print(bleh)
#Remove item from list
if "Pierogi" in bleh:
  bleh.remove("Pierogi")
if "Horse meat" in bleh:
  bleh.remove("Horse meat")
print(bleh)
#Remove item by Index
x = bleh.pop(1) #removed but stored in X variable
print(bleh)
print(x*8)
#Alternative way of deleting item via index
del bleh[2]
print(bleh)
#Extending list by another list
yummy.extend(bleh)
print(yummy)
print(bleh)
#Mutating a list
yummy[4] = "Hamburger"
yummy[1] = "666"
print(yummy)
#Check a list for particular data type/traverse a list
lista = ["Fred", 56, True, "Piotr", -4.8, "Ham", 89, False]
for item in lista:
  if isinstance(item, str) or isinstance(item, float):
    print(item, end = " ")