def interests():
  print("Enter all your interests, one after the other and enter \"stop\" when done")
  s1 = set()
  while True:
    interest = input()
    if interest.lower() == "stop":
      break
    else:  
      s1.add(interest)
  return s1
print(interests())

def tinderDaSecond():
  print("First person: ")
  p1 = interests()
  print("Second person: ")
  p2 = interests()
  common = p1.intersection(p2)
  if len(common) >= 3:
    print(f"You are matching <3, you have {len(common)} common interests")
  else:
    print("Asta e , cand nu merge nu merge")

tinderDaSecond()