import json

from ui.banner import box_line_downwards, box_line_upwards
from ui.colors import BLUE, GREEN, MAGENTA, RED, RESET, YELLOW


def view_data():
    with open("database/data.json") as file:
        data = json.load(file)
    for name in data:
        box_line_downwards()
        print(f" {GREEN}Student     :{RESET} {BLUE}{name.capitalize()}{RESET}")

        for subject in data[name]:
            print(
                f" {YELLOW}{subject:<12}{RESET}: {MAGENTA}{data[name][subject]}{RESET}"
            )
        box_line_upwards()
