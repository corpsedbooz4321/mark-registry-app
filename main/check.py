# check.py
from data import registry
from data import subject


def check_result():
    while True:
        print("\n===== Check your result by Entering your name =====")
        name = input("\nEnter your name(or press q for main Menu): ").lower()
        if name == "q":
            return

        if not name.replace(" ", "").isalpha():
            print("Invalid Name!, Use Non-numeric names!")
            continue

        if name in registry:
            print(f"Student: {name}")
            print(f"Subject: {subject}")
            print(f"Marks: {registry[name]}%")
        else:
            print("No result found with the given name!")
