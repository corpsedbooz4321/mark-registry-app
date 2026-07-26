# Script that holds the fuction removes or deletes the entry!!
import json

from ui.banner import box_line_downwards, box_line_upwards, show_line
from ui.colors import BLUE, GREEN, MAGENTA, RED, RESET, YELLOW


def clean_empty_student(data, name):
    if len(data[name]) == 0:
        print(f"{MAGENTA}{name}{RESET} {RED}has no data left.")
        while True:
            choice = input(f"{RED}Delete{RESET} the student as well? (y/n): ").lower()
            if choice == "y":
                del data[name]
                print(f"{GREEN}Student {BLUE}{name}{RESET} deleted successfully!!")
                with open("maindata/data.json", "w") as file:
                    json.dump(data, file, indent=2)
                display_student(data, name)
                return
            elif choice == "n":
                break


def display_student(data, name):
    if name in data:
        box_line_downwards()
        print(f" {GREEN}Student{RESET} : {BLUE}{name}{RESET}")
        for subject in data[name]:
            print(f" {YELLOW}{subject}{RESET}: {MAGENTA}{data[name][subject]}{RESET}")
        box_line_upwards()


def remove():
    show_line(2)
    with open("maindata/data.json") as file:
        data = json.load(file)
    name = input(f"{YELLOW}Enter your name: {RESET}")
    if name not in data:
        print(f"{RED}The name {name} not found!!{RESET}")
        return
    display_student(data, name)
    while True:
        subject_removal = input(
            f"{YELLOW}\nEnter the name of the subject: {RESET}"
        ).lower()
        if subject_removal == "q":
            return
        if subject_removal == "done":
            with open("maindata/data.json", "w") as file:
                json.dump(data, file, indent=2)
            print(f"{GREEN}\nChanges saved successfully!!{RESET}")
            # display_student(data, name)
            return
        if not subject_removal.replace(" ", "").isalpha():
            print(f"{RED}Invalid name!, use Non-numeric names..!!{RESET}")
            continue

        if subject_removal in data[name]:
            del data[name][subject_removal]
            print(
                f"{GREEN}Removal of the {subject_removal} from {name} finished! '{RED}done{RESET}' to save! '{RED}q{RESET}' to discard.."
            )
            display_student(data, name)

        else:
            print(f"{RED}Subject {subject_removal} not found!{RESET}")
    else:
        print(f"{RED}The name {name} not found!!{RESET}")
