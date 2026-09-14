# check_entry.py
import json

from src.features.diplay_results import print_result
from src.helper.database import DATA_FILE
from src.ui.banner import show_line
from src.ui.colors import RED, RESET, YELLOW


def check_result():
    with DATA_FILE.open() as file:
        student_data = json.load(file)
    # result_banner()
    show_line()
    while True:
        name = input(f"\n{YELLOW}Enter your name('q' for main Menu): {RESET}").lower()
        if name == "q":
            return

        if not name.replace(" ", "").isalpha():
            print(f"\n{RED}Invalid Name!, Use Non-numeric names!{RESET}")
            continue

        if name in student_data:
            print_result(student_data, name)
        else:
            print(f"\n{RED}No results found with the given name!{RESET}")
