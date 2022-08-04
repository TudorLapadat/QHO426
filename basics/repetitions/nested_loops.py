seq = input("Please enter a sequence:")
marker = input("Please enter a marker:")
pos1 = 99
pos2 = 99

for i in range (0, len(seq)):
  if (seq[i] == marker):
    if pos1 == 99:
      pos1 = i
    else:
      pos2 = i
print(f"The distance between the markers is {pos2-pos1-1}")