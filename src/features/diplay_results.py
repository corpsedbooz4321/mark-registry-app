# Printing results
from src.ui.banner import box_line_downwards, box_line_upwards
from src.ui.colors import GREEN, MAGENTA, RED, RESET, YELLOW
from src.utils.average import calculate_average


def print_result(student_data, name):
    marks = student_data[name]
    print(f"{GREEN}Success...{RESET}")
    box_line_downwards()
    print(f"{name.title():^40}")
    for subject, mark in marks.items():
        col = ":"
        print(
            f"  {GREEN}{subject.title():<17}{RESET}{col.center(1)} {MAGENTA}{mark:>15}{RESET}%"
        )
    box_line_upwards()
    box_line_downwards()
    average = calculate_average(marks)
    avg = "Average"
    col = ":"
    print("statistics".center(40))
    if 100 >= average >= 80:
        print(f"  {GREEN}{avg:<17}{RESET}{col.center(1)}{GREEN}{average:>17}{RESET}%")
        # return
    elif 80 > average >= 30:
        print(f"  {GREEN}{avg:<17}{RESET}{col.center(1)}{YELLOW}{average:>17}{RESET}%")
    else:
        print(f"  {GREEN}{avg:<17}{RESET}{col.center(1)}{RED}{average:>17}{RESET}%")
    box_line_upwards()
