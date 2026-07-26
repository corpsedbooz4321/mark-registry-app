# main.py
from features.check import check_result
from features.delete_entry import remove
from features.instructions import instruction
from features.update import update_result
from features.view_all import view_data
from ui.banner import big_line, show_banner, show_line
from ui.colors import GREEN, RED, RESET, YELLOW

show_banner()
show_line()


def menu():
    while True:
        print(f"(A) {GREEN}To list all available data.{RESET}")
        print(f"(C) {GREEN}To Check the result.{RESET}")
        print(f"(D) {GREEN}To Remove a entry.{RESET}")
        print(f"(U) {GREEN}To Update the result.{RESET}")
        print(f"(Q) {RED}To Exit{RESET}")
        print(f"(H) {GREEN}Help?")
        user_input = input(f"{YELLOW}Enter your choice[a, c, d, u, q]: {RESET}").lower()

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
