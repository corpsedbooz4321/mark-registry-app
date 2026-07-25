# check.py
import json
import re

from banner import (box_line_downwards, box_line_upwards, result_banner,
                    show_line)
from colors import GREEN, MAGENTA, RED, RESET, WHITE, YELLOW


def check_result():
    with open("data.json") as file:
        student_data = json.load(file)
    result_banner()
    show_line()
    while True:
        name = input(f"\n{YELLOW}Enter your name('q' for main Menu): {RESET}").lower()
        if name == "q":
            return

        if not name.replace(" ", "").isalpha():
            print(f"{RED}Invalid Name!, Use Non-numeric names!{RESET}")
            continue

        if name in student_data:
            marks = student_data[name]
            print(f"{GREEN}Success...{RESET}")
            box_line_downwards()
            print(f" Student: {name.title()}")
            for subject, mark in marks.items():
                print(f" {GREEN}{subject.title()}{RESET}: {mark}%")
            box_line_upwards()
        else:
            print(f"{RED}No results found with the given name!{RESET}")
