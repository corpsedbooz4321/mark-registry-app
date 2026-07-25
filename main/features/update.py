# update.py
import json

from ui.banner import show_line, update_banner
from ui.colors import GREEN, MAGENTA, RED, RESET, YELLOW


def update_result():
    update_banner()
    show_line()
    with open("maindata/data.json") as file:
        data = json.load(file)
    while True:
        new_name = input(f"\n{YELLOW}Name to update(or 'q' to menu): {RESET}").lower()
        if new_name == "q":
            return
        if not new_name.replace(" ", "").isalpha():
            print(f"{RED}Invalid name!, use Non-numeric names...!!{RESET}")
            continue
        if new_name not in data:
            data[new_name] = {}

        while True:
            subject = input(
                f"\n{YELLOW}Enter the name of the subjects: {RESET}"
            ).lower()
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
                    data[new_name][subject] = mark
                    print(
                        f"{GREEN}Success! {new_name}'s data has been added 'done' to save all the changes!{RESET}"
                    )
                    break
                print(f"\n{RED}Marks must be between 0 and 100.{RESET}")
