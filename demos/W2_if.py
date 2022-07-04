name = input("Enter your name: ")
#len() - function that returns the length of an item, you put inside of it.

if len(name) > 8:
  print("Your name is very long , please tell me a nickname: ")
  name = input()
elif len(name) <= 3:
  print("Your name is super short.")
elif name.upper() == "MARTHA": #oricum scrii numele il recunoaste
  print("Why did you said that name?!")
else:
  print("You have a meh name!")
print(f"Welcome {name}!")