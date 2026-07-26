# update.py
import json

from features.delete_entry import display_student
from ui.banner import show_line, update_banner
from ui.colors import BLUE, GREEN, MAGENTA, RED, RESET, YELLOW


def update_result():
    # update_banner()
    show_line()
    with open("maindata/data.json") as file:
        data = json.load(file)
    while True:
        name = input(f"\n{YELLOW}Name to update(or 'q' to menu): {RESET}").lower()
        if name == "q":
            return
        if not name.replace(" ", "").isalpha():
            print(f"{RED}Invalid name!, use Non-numeric names...!!{RESET}")
            continue
        if name in data:
            print(f"\n{BLUE}Preview")
            display_student(data, name)

        if name not in data:
            data[name] = {}

        while True:
            subject = input(
                f"\n{YELLOW}Enter the name of the subjects: {RESET}"
            ).lower()
            if subject == "q":
                return
            if subject == "done":
                with open("maindata/data.json", "w") as file:
                    json.dump(data, file, indent=2)
                print("Finished..!!")
                return
            if not subject.replace(" ", "").isalpha():
                print(f"{subject}, {RED}Invalid subject name..{RESET}")
                continue
            while True:

                try:
                    mark = int(input(f"{YELLOW}Enter marks: {RESET}"))

                except ValueError:
                    print(f"{RED}Invalid input, Marks must be a number!!{RESET}")
                    continue
                if 0 <= mark <= 100:
                    data[name][subject] = mark
                    display_student(data, name)
                    print(
                        f"{GREEN}Success! {name}'s data has been added 'done' to save 'q' to discard!{RESET}"
                    )
                    break
                print(f"\n{RED}Marks must be between 0 and 100.{RESET}")
