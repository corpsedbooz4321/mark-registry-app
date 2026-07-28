from ui.banner import show_line
from ui.colors import BLUE, GREEN, MAGENTA, RED, RESET, YELLOW


def instruction():
    show_line()
    show_line()
    print(f"\n{MAGENTA}=== Mark Registry App Help ==={RESET}")
    print(f"{YELLOW}How to start the app:{RESET}")
    print("  From the project root: python3 Mark-Registry-App/Mark-Registry-App.py")
    print(
        "  Or from the Mark-Registry-App folder: cd Mark-Registry-App && python3 Mark-Registry-App.py"
    )
    print()

    print(f"{YELLOW}Mark-Registry-App menu commands:{RESET}")
    print(f"  {GREEN}(A){RESET} View all saved student data")
    print(
        f"    -> handled in {BLUE}Mark-Registry-App/features/view_all.py{RESET} -> view_data()"
    )
    print(f"  {GREEN}(C){RESET} Check a student's marks")
    print(
        f"    -> handled in {BLUE}Mark-Registry-App/features/check.py{RESET} -> check_result()"
    )
    print(f"  {GREEN}(D){RESET} Remove marks or delete a student entry")
    print(
        f"    -> handled in {BLUE}Mark-Registry-App/features/delete_entry.py{RESET} -> remove()"
    )
    print(f"  {GREEN}(U){RESET} Update or add marks for a student")
    print(
        f"    -> handled in {BLUE}Mark-Registry-App/features/update.py{RESET} -> update_result()"
    )
    print(f"  {GREEN}(H){RESET} Show this help screen")
    print(
        f"    -> handled in {BLUE}Mark-Registry-App/features/instructions.py{RESET} -> instruction()"
    )
    print(f"  {RED}(Q){RESET} Exit the application")
    print()

    print(f"{YELLOW}How each feature works:{RESET}")
    print(f"  {GREEN}Check result{RESET}")
    print("    - Enter the student's name.")
    print("    - Type 'q' to return to the Mark-Registry-App menu.")
    print("    - Only non-numeric names are accepted.")

    print(f"  {GREEN}Update result{RESET}")
    print("    - Enter the student's name.")
    print("    - Enter a subject name and then its marks.")
    print("    - Marks must be between 0 and 100.")
    print("    - Type 'done' to save all changes.")
    print("    - Type 'q' to discard and return to the Mark-Registry-App menu.")

    print(f"  {GREEN}Remove entry{RESET}")
    print("    - Enter the student's name.")
    print("    - Enter the subject name to remove it.")
    print("    - Type 'done' to save changes.")
    print("    - Type 'q' to leave the remove screen.")
    print("    - If no marks are left, you can choose to delete the student as well.")

    print(f"  {GREEN}View all data{RESET}")
    print("    - Shows every saved student and their subjects/marks.")

    print(f"{YELLOW}Where the data is stored:{RESET}")

    print(f"  {BLUE}main/database/data.json{RESET}")

    print("  All changes are saved into this JSON file.")

    print(f"{YELLOW}Where the commands are connected:{RESET}")
    print("  - The menu loop is in Mark-Registry-App/Mark-Registry-App.py")
    print(
        "  - Each letter choice calls a feature function from the Mark-Registry-App/features folder"
    )
    print("  - The app uses the UI colors and banner helpers from Mark-Registry-App/ui")
    print()
