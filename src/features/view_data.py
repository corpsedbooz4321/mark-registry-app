import json

from src.helper.database import DATA_FILE
from src.ui.banner import box_line_downwards, box_line_upwards
from src.ui.colors import BLUE, GREEN, MAGENTA, RESET, YELLOW


def view_data():
    with DATA_FILE.open() as file:
        data = json.load(file)
    for name in data:
        box_line_downwards()
        print(f" {GREEN}Student     :{RESET} {BLUE}{name.capitalize()}{RESET}")

        for subject in data[name]:
            print(
                f" {YELLOW}{subject:<12}{RESET}: {MAGENTA}{data[name][subject]}{RESET}"
            )
        box_line_upwards()
