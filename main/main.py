# main.py
from banner import show_banner, show_line
from check import check_result
from update import update_result

show_banner()
show_line()


def menu():
    while True:
        print("(c) tm Check the result.")
        print("(u) to Update the result.")
        print("(q) to Exit")
        user_input = input("Choose what to perform [c, u, q]: ").lower()

        if user_input == "c":
            check_result()  # Calls function inside check.py
        elif user_input == "u":
            update_result()  # Calls function inside update.py
        elif user_input == "q":
            print("Exiting....")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    menu()
