from ui.colors import BLUE, GREEN, MAGENTA, RED, RESET, YELLOW


def instruction():
    print(f"\n{MAGENTA}=== Mark Registry App Help ==={RESET}")
    print(f"{YELLOW}How to start the app:{RESET}")
    print("  From the project root: python3 main/main.py")
    print("  Or from the main folder: cd main && python3 main.py")
    print()

    print(f"{YELLOW}Main menu commands:{RESET}")
    print(f"  {GREEN}(A){RESET} View all saved student data")
    print(f"    -> handled in {BLUE}main/features/view_all.py{RESET} -> view_data()")
    print(f"  {GREEN}(C){RESET} Check a student's marks")
    print(f"    -> handled in {BLUE}main/features/check.py{RESET} -> check_result()")
    print(f"  {GREEN}(D){RESET} Remove marks or delete a student entry")
    print(f"    -> handled in {BLUE}main/features/delete_entry.py{RESET} -> remove()")
    print(f"  {GREEN}(U){RESET} Update or add marks for a student")
    print(f"    -> handled in {BLUE}main/features/update.py{RESET} -> update_result()")
    print(f"  {GREEN}(H){RESET} Show this help screen")
    print(f"    -> handled in {BLUE}main/features/instructions.py{RESET} -> instruction()")
    print(f"  {RED}(Q){RESET} Exit the application")
    print()

    print(f"{YELLOW}How each feature works:{RESET}")
    print(f"  {GREEN}Check result{RESET}")
    print("    - Enter the student's name.")
    print("    - Type 'q' to return to the main menu.")
    print("    - Only non-numeric names are accepted.")

    print(f"  {GREEN}Update result{RESET}")
    print("    - Enter the student's name.")
    print("    - Enter a subject name and then its marks.")
    print("    - Marks must be between 0 and 100.")
    print("    - Type 'done' to save all changes.")
    print("    - Type 'q' to discard and return to the main menu.")

    print(f"  {GREEN}Remove entry{RESET}")
    print("    - Enter the student's name.")
    print("    - Enter the subject name to remove it.")
    print("    - Type 'done' to save changes.")
    print("    - Type 'q' to leave the remove screen.")
    print("    - If no marks are left, you can choose to delete the student as well.")

    print(f"  {GREEN}View all data{RESET}")
    print("    - Shows every saved student and their subjects/marks.")

    print(f"{YELLOW}Where the data is stored:{RESET}")
    print(f"  {BLUE}main/maindata/data.json{RESET}")
    print("  All changes are saved into this JSON file.")

    print(f"{YELLOW}Where the commands are connected:{RESET}")
    print("  - The menu loop is in main/main.py")
    print("  - Each letter choice calls a feature function from the main/features folder")
    print("  - The app uses the UI colors and banner helpers from main/ui")
    print()
