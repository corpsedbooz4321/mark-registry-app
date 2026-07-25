# main.py
from banner import show_banner, show_line
from check import check_result
from colors import GREEN, RED, RESET, YELLOW
from update import update_result

show_banner()
show_line()


def menu():
    while True:
        print(f"(C) {GREEN}To Check the result.{RESET}")
        print(f"(A) {GREEN}To list all data.{RESET}")
        print(f"(U) {GREEN}To Update the result.{RESET}")
        print(f"(Q) {RED}To Exit{RESET}")
        user_input = input(f"{YELLOW}Choose what To perform [c, u, q]: {RESET}").lower()

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
