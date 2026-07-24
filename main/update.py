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
                print("Exiting..")
                break
            if not subject.replace(" ", "").isalpha():
                print(f"{subject}, Invalid subject name..")
                continue
            try:
                while True:
                    mark = int(input(f"\nEnter the marks obtained: "))
                    if 0 <= mark <= 100:
                        registry[new_name][subject] = mark
                        print(
                            f"Success! {new_name} data has been added!, {mark} in {subject}"
                        )
                        break
                    else:
                        print("\nMarks must be between 0 to 100!")
                        continue
            except ValueError:
                print("Invalid input! Please enter a numeric value for marks.")
