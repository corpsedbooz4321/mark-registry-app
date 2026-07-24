# update.py

from data import registry


def update_result():
    while True:
        new_name = input("\nName to update(or 'q' to menu): ").lower()
        if new_name == "q":
            return
        if not new_name.replace(" ", "").isalpha():
            print("Invalid name!, use Non-numeric names...!!")
            continue
        if new_name not in registry:
            registry[new_name] = {}

        while True:
            subject = input("\nEnter the name of the subjects: ").lower()
            if subject == "done":
                print("Finished..!!")
                break
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
                    registry[new_name][subject] = mark
                    print(f"Success! {new_name}'s data has been added/updated")
                    break
                print("\nMarks must be between 0 and 100.")
