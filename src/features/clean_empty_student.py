import json

from src.helper.database import DATA_FILE
from src.ui.colors import BLUE, GREEN, MAGENTA, RED, RESET


def clean_empty_student(data, name):
    if not (data[name]):
        print(f"\n{MAGENTA}{name}{RESET} {RED}has no data left.")
        while True:
            choice = (
                input(f"{RED}Delete{RESET} the student as well? (y/n): ")
                .strip()
                .lower()
            )
            if choice == "y":
                del data[name]
                print(f"{GREEN}Student {BLUE}{name}{RESET} deleted successfully!!")
                with DATA_FILE.open("w") as file:
                    json.dump(data, file, indent=2)
                return True
            elif choice == "n":
                return True
            else:
                print(f"{RED}Choose from above options!!")
    return False
