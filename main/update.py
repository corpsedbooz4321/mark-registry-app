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

        subject = input("\nEnter the name of the subject: ").lower()
        if not subject.replace(" ", "").isalpha():
            print("Invalid subject!, Use Non-numeric subject names...!")
            continue

        try:
            mark = int(input(f"Enter your marks for {new_name}: "))

            if 0 <= mark <= 100:
                registry[new_name] = {"subject": subject, "mark": mark}
                print(f"Success! {new_name} results has been added!, {mark} in {subject}")
            else:
                print("Marks must be between 0 to 100!")
        except ValueError:
            print("Invalid input! Please enter a numeric value for marks.")
