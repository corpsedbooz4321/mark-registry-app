# update.py

from data import registry


def update_result():
    while True:
        new_name = input("\nName to update(or 'q' to menu): ").lower()
        if new_name == "q":
            return
        if not new_name.replace(" ", "").isalpha():
            print("Invalid name!, use Non-numeric names...!!")

        try:
            mark = int(input(f"Enter your marks for {new_name}: "))

            if 0 <= mark <= 100:
                registry[new_name] = mark
                print(f"Success!{new_name} marks added!, {mark}")
            else:
                print("Marks must be between 0 to 100!")
        except ValueError:
            print("Invalid input! Please enter a numeric value for marks.")
