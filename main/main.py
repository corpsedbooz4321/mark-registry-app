# main.py

from features.check import check_result
from features.update import update_result
from features.view_all import view_data
from ui.banner import show_banner, show_line
from ui.colors import GREEN, RED, RESET, YELLOW

show_banner()
show_line()


def menu():
    while True:
        print(f"(C) {GREEN}To Check the result.{RESET}")
        print(f"(A) {GREEN}To list all available data.{RESET}")
        print(f"(U) {GREEN}To Update the result.{RESET}")
        print(f"(Q) {RED}To Exit{RESET}")
        user_input = input(f"{YELLOW}Choose what To perform [c, u, q]: {RESET}").lower()

        if user_input == "c":
            check_result()  # Calls function inside check.py
        elif user_input == "a":
            view_data()
        elif user_input == "u":
            update_result()  # Calls function inside update.py
        elif user_input == "q":
            print("Exiting....")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    menu()
