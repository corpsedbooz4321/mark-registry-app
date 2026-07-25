# check.py
import json
import re

from banner import (box_line_downwards, box_line_upwards, result_banner,
                    show_line)


def check_result():
    with open("data.json") as file:
        student_data = json.load(file)
    result_banner()
    show_line()
    while True:
        name = input("\nEnter your name(or press q for main Menu): ").lower()
        if name == "q":
            return

        if not name.replace(" ", "").isalpha():
            print("Invalid Name!, Use Non-numeric names!")
            continue

        if name in student_data:
            marks = student_data[name]
            box_line_downwards()
            print(f" Student: {name.title()}")
            for subject, mark in marks.items():
                print(f" {subject.title()}: {mark}%")
            box_line_upwards()
        else:
            print("No results found with the given name!")
