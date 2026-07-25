# Script that holds the fuction removes or deletes the entry!!
import json
from warnings import resetwarnings

from ui.banner import box_line_downwards, box_line_upwards
from ui.colors import BLUE, GREEN, MAGENTA, RED, RESET, YELLOW


def remove():
    print("========== Removing entries ==========")

    with open("maindata/data.json") as file:
        data = json.load(file)

    name = input(f"{YELLOW}Enter your name: {RESET}")
    if name in data:
        box_line_downwards()
        print(f" {GREEN}Student{RESET} : {BLUE}{name}{RESET}")
        for subject in data[name]:
            print(f" {YELLOW}{subject}{RESET}: {MAGENTA}{data[name][subject]}{RESET}")
        box_line_upwards()
    subject_removal = input(f"{YELLOW}Enter subject: {RESET}")

