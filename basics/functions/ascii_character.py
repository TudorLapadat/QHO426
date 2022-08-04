print("Program started!")
print("Please enter a ASCII code: ")
x = int(input())
if x in range(32,127):
  print(f"The character represented by ASCII code {x} is {chr(x)}")

print("The program ended!")