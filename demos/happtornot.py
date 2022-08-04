h = input("Are you happy? Y/N:")
k = input("Do you know it? Y/N:")
if h.upper() =="Y" and k.upper() == "Y":
  print("Clap your hands!")
elif h.upper() == "N" and k.upper() == "N":
  print("Boo-Hooo")
elif h.upper() == "N":
  print("Cheer up boss!")
elif k.upper() == "N":
  print("Sure my friend?")
else:
  print("This is not achievable")