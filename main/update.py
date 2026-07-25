# update.py
import json


def update_result():
    with open("data.json") as file:
        data = json.load(file)
    while True:
        new_name = input("\nName to update(or 'q' to menu): ").lower()
        if new_name == "q":
            return
        if not new_name.replace(" ", "").isalpha():
            print("Invalid name!, use Non-numeric names...!!")
            continue
        if new_name not in data:
            data[new_name] = {}

        while True:
            subject = input("\nEnter the name of the subjects: ").lower()
            if subject == "done":
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=2)
                print("Finished..!!")
                return
            if not subject.replace(" ", "").isalpha():
                print(f"{subject}, Invalid subject name..")
                continue
            while True:

                try:
                    mark = int(input("Enter marks: "))

                except ValueError:
                    print("Invalid input, Marks must be a number!!")
                    continue
                if 0 <= mark <= 100:
                    data[new_name][subject] = mark
                    print(f"Success! {new_name}'s data has been added/updated")
                    break
                print("\nMarks must be between 0 and 100.")
