import json

from ui.banner import box_line_downwards, box_line_upwards


def view_data():
    with open("maindata/data.json") as file:
        data = json.load(file)
    for name in data:
        box_line_downwards()
        print(f"Student:  {name}")

        for subject in data[name]:
            print(f" {subject}: {data[name][subject]}")
        box_line_upwards()
