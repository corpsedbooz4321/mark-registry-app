# Script that holds the fuction removes or deletes the entry!!
import json
from re import sub

from ui.colors import BLUE, GREEN, MAGENTA, RED, RESET, YELLOW

print("========== Removing entries ==========")

def user_input(data):
    name = input(f"{YELLOW}Enter your name: {RESET}").lower()
    if name in data["name"]:
        removal = input(f"{YELLOW}Enter which subject you want to remove: {RESET}")
        if removal in data["name"][name]["subject"]:
            del data["name"][name]["subject"][removal]
            print(f"{GREEN}Data removal of {removal} from the {name} is done!!")
    else:
        print(f"{RED}subject not found!!{RESET}")
            






def delete():
    with open("maindata/data.json") as file:
        data = json.load(file)
        user_input()
        print(f"Data related to the {BLUE}{name}{RESET} found!!")
        print(f"{GREEN}(D) To delete a student. {RESET}")
        print(f"{GREEN}(E) To delete a student's entries. {RESET}")
        choice = input(f"{YELLOW}Choice: {RESET}").lower()
        if choice == 1:
            pass
        name = input(f"{YELLOW}Enter your name: {RESET}").lower()
        if name in data[name]: