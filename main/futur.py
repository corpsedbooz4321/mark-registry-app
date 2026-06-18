main_registry = {
    "aditya": 65,
    "rahul": 67,
    "mahim": 70,
    "ankit": 96
}


#Name check block.
def student_result(name):
    while True:
        name = input("Enter your name: ").lower()
        if not name.replace(" ", "").isalpha():
            print("Invalid input, Names can't be in numeric form...")
            continue
        elif name in main_registry:
            print('Name is present in the list!')
        else:
            print('Name is not present in the list!')

        
# def result_update():
#     while True:
#         student_name = input("Enter the name of the student: ").lower
#         if not student_name.replace(' ', '').isalpha():
#             print("Invalid input!, Names must be in non numeric form...")
#         student_marks = int(input("Enter the marks of the student: "))
#         if student_marks > 100 or student_marks < 0:
#             print("Invalid marks!")
#         else:
#             result_update.append(student_name, student_marks)


def menu():
    print('\n=================' \
    ' Welcome To Mark Registry App =================')
    while True:
        print('\n Menu')
        print("\n(y) To check, the students result!.")
        print("(n) To update or add the a students result.")
        print("(q) To exit.")
        choice = (input("Choose: ")).lower()
        if choice == "y":
            student_result(name)
        # elif choice == "n":
        #     list_update()
        # elif choice == "q":
        #     print("Goodbye!")
        #     break
        else:
            print("invalid choice!")
menu()