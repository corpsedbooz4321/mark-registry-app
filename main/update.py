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
            continue

        while True:
            subject = input("\n Enter the name of the subjects: ").lower()

            if subject == "done":
                break

        try:
            mark = int(input(f"Enter your marks for {new_name}: "))

            if 0 <= mark <= 100:
                registry[new_name] = {"subject": subject, "mark": mark}
                print(
                    f"Success! {new_name} results has been added!, {mark} in {subject}"
                )
            else:
                print("Marks must be between 0 to 100!")
        except ValueError:
            print("Invalid input! Please enter a numeric value for marks.")
