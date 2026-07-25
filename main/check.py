# check.py
import json


def check_result():
    with open("data.json") as file:
        student_data = json.load(file)
    while True:
        print("\n===== Check your result by Entering your name =====")
        name = input("\nEnter your name(or press q for main Menu): ").lower()
        if name == "q":
            return

        if not name.replace(" ", "").isalpha():
            print("Invalid Name!, Use Non-numeric names!")
            continue

        if name in student_data:
            marks = student_data[name]
            print(f"\nStudent: {name.title()}")
            for subject, mark in marks.items():
                print(f"{subject.title()}: {mark}%")
        else:
            print("No results found with the given name!")
