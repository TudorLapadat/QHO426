while True:
  print("Please choose one of the folowing options: \n1-Nice message\n2-Area of rectangle\n3-Area of a triangle\n4-Times table\n5-Exit")
  opt = int(input())
  if opt == 1:
    print("You do not smell too bad today<3")
  elif opt == 2:
    h = float(input("Enter height: "))
    w = float(input("Enter width: "))
    print(f"The area is {h*w}cm^2")
  elif opt == 3:
    h = float(input("Enter height: "))
    b = float(input("Enter width: "))
    print(f"The area is {h*b*0.5}cm^2")
  elif opt == 4:
    n = int(input("Enter all number: "))
    for i in range (1, 11):
      print(f"{n}x{i}={n*i}")
    print("thats all folks!")
  elif opt == 5:
    break
  else:
    print("Constanta mai da-mi!")
   