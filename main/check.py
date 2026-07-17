# check.py
from data import registry


def check_result():
    while True:
        print("\n===== Check your result by Entering your name =====")
        name = input("\nEnter your name(or press q for main Menu): ").lower()
        if name == "q":
            return

        if not name.replace(" ", "").isalpha():
            print("Invalid Name!, Use Non-numeric names!")
            continue

        if name in registry:
            student_data = registry[name]
            print(f"Student: {name}")
            print(f"Subject: {student_data['subject']}")
            print(f"Marks: {student_data['mark']}%")
        else:
            print("No result found with the given name!")
