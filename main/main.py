list = ["happy", "rohan", "aditya", "rahul", "sujal"]# A temperory list
#name check block
def name_check():
    while True:
        name = input("\nEnter your name(or 'q' to back to main menu): ").lower()
        if not name.isalpha():
            print("Invalid input! Use non-numeric names...")
            continue
        if name in list:
            print("The given name is already present in the list!")
        elif name == 'q':
            menu()
        else:
            print("Name is not present in the list")
#list updating block
def list_update():
    while True:
      name1 = input("\nEnter a name to add or (q to go to main menu): ").lower()
      if not name1.isalpha():
          print("Invalid input! Use non-numeric names...")
          continue 
      if name1 == "q":
          print("\nreturning to main menu..")
          menu()
          break
      list.append(name1)
      print(f"{name1} has been added to the list!")
#menu block
def menu():
    print('\n=================' \
    ' Welcome To Mark Registry App =================')
    print('\n Menu')
    print("\n(y) To check, if the name is present in the list or not.")
    print("(n) To update or add a name in the list.")
    print("(q) To exit.")
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
menu()