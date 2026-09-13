# main.py
from src.features.check import check_result
from src.features.delete_entry import remove
from src.features.instructions import instruction
from src.features.update import update_result
from src.features.view_all import view_data
from src.helper.setup_dirs import setup_missing_dirs
from src.ui.banner import show_banner, show_line
from src.ui.colors import GREEN, RED, RESET, YELLOW

show_banner()
show_line()

setup_missing_dirs()


def menu():
    while True:
        print(f"(A) {GREEN}To list all available data.{RESET}")
        print(f"(C) {GREEN}To Check the result's.{RESET}")
        print(f"(D) {GREEN}To Delete Registry's.{RESET}")
        print(f"(U) {GREEN}To Update Registry's.{RESET}")
        print(f"(Q) {RED}To Exit{RESET}")
        print(f"(H) {GREEN}Help?")
        user_input = input(
            f"{YELLOW}Enter your choice[a, c, d, h, u, q]: {RESET}"
        ).lower()

        if user_input == "c":
            check_result()  # Calls function inside check.py
        elif user_input == "a":
            view_data()
        elif user_input == "d":
            remove()
        elif user_input == "h":
            instruction()
        elif user_input == "u":
            update_result()  # Calls function inside update.py
        elif user_input == "q":
            print(f"\n{RED}Exiting....{RESET}")
            break
        else:
            print(f"{RED}Invalid choice!{RESET}")


if __name__ == "__main__":
    menu()
