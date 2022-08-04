#Initialise an empty set
s = {1,2}
print(type(s))
#Initialise non-empty set
colours = {"blue", "red", "yellow", "purple"}
print(colours)
#Adding elements to a set
colours.add("green")
print(colours)
#remove item from a set
if"red" in colours:
  colours.remove("red")
if "turqoise" in colours:
  colours.remove("turqoise")
print(colours)
#Sets are heterogenous and duplicates are not allowed
colours.add(99)
colours.add(False)
colours.add("blue")
print(colours)