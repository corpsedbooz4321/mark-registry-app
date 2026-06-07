l = ["happy", "rohan", "aditya", "rahul", "sujal"]
# print(type(l))
def name_check():
    name = input("Enter your name: ").lower()

    if name in l:
        print("The given name is already present in the list!")
    else:
        print("The given name is not present in the list!")
def list_update():
    while True:   
      name1 = input("\nEnter a name to add or (q)exit: ").lower()
      if name1 == "q":
          print("\nreturning to main menu..")
          menu()
          break
      l.append(name1)
      print(f"{name1} has been added to the list!")




def menu():
    print("\n(y) to check, if the name is present in the list or not.")
    print("(n) to update or add a name in the list.")
    print("(q) to exit.")
menu()

while True:
    choice = (input("Choose: ")).lower()
    if choice == "y":
        name_check()
    elif choice == "n":
        list_update()
    elif choice == "q":
        print("Goodbye!")
        break
    else:
        print("invalid choice!")