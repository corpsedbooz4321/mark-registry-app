registry = {"aditya": 64, "mahima": 66}


def update_result():
    while True:
        new_name = input(
            'Enter name to update or "(q)" to go back to main menu: '
        ).lower()
        if new_name == "q":
            return
        if not new_name.replace(" ", "").isalpha():
            print("Invalid name!, use Non-numeric names...!!")

        try:
            mark = int(input(f"Enter your marks for {new_name}: "))

            if 0 <= mark <= 100:
                registry[new_name] = mark
                print(f"Success! {new_name} has been updated with marks, {mark}")
            else:
                print("Marks must be between 0 to 100!")
        except ValueError:
            print("Invalid input! Please enter a numeric value for marks.")


# the block that checks the result.
def check_result():
    while True:
        print("\n===== Check you result by Entering your name =====")
        name = input("\nEnter your name(or press q for main Menu): ").lower()
        if name == "q":
            return
        if not name.replace(" ", "").isalpha():
            print("Invalid Name!, Use Non-numeric names!")
        elif name in registry:
            print(f"The result of {name} is: {registry[name]}%")
        else:
            print("No result found with the given name!")


# menu block
def menu():
    while True:
        print("\n==========Mark Registry App==========")
        print("\n(c) to Check the result.")
        print("(u) to Update the result.")
        print("(q) to Exit")
        user_input = input("Choose what to perform[c, u, q]: ").lower()

        if user_input == "c":
            check_result()
        elif user_input == "u":
            update_result()
        elif user_input == "q":
            print("Exiting....")
            break
        else:
            print("Invalid choice!")


menu()
