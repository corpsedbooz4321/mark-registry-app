# averate calculator
import json


def average():
    with open("database/data.json") as file:
        data = json.load(file)
