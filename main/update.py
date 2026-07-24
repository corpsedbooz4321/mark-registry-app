# update.py

from data import registry


def update_result():
    while True:
        new_name = input("\nName to update(or 'q' to menu): ").lower()
        if new_name == "q":
            return
        if not new_name.replace(" ", "").isalpha():
            print("Invalid name!, use Non-numeric names...!!")
        if new_name not in registry:
            registry[new_name] = {}

        while True:
            subject = input("\nEnter the name of the subjects: ").lower()
            if not subject.replace(" ", "").isalpha():
                print(f"{subject}, Invalid subject name..")
                continue
            if subject == "done":
                break
            try:
                mark = int(input(f"Enter the marks obtained: "))
                if 0 <= mark <= 100:
                    registry[new_name][subject] = mark

                    print(
                        f"Success! {new_name} data has been added!, {mark} in {subject}"
                    )
                else:
                    print("Marks must be between 0 to 100!")
            except ValueError:
                print("Invalid input! Please enter a numeric value for marks.")
