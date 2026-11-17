
import os
from datetime import datetime

FILE_NAME = "diary.txt"
PASSWORD = "1234"


def login():
    print("=" * 35)
    print("       PERSONAL DIARY APP")
    print("=" * 35)

    password = input("Enter password: ")

    if password == PASSWORD:
        print("\nLogin successful!")
        return True
    else:
        print("\nWrong password!")
        return False


def add_entry():
    print("\n--- Add New Entry ---")

    title = input("Enter title: ")
    content = input("Write your thoughts: ")

    if title == "" or content == "":
        print("Title and content cannot be empty!")
        return

    date = datetime.now().strftime("%d-%m-%Y %H:%M")

    with open(FILE_NAME, "a") as file:
        file.write(f"\nDATE: {date}\n")
        file.write(f"TITLE: {title}\n")
        file.write(f"CONTENT: {content}\n")
        file.write("-" * 35 + "\n")

    print("\nEntry saved successfully!")


def view_entries():
    print("\n--- Your Diary Entries ---")

    if not os.path.exists(FILE_NAME):
        print("No diary entries found.")
        return

    with open(FILE_NAME, "r") as file:
        data = file.read()

    if data.strip() == "":
        print("Your diary is empty.")
    else:
        print(data)


def search_entry():
    print("\n--- Search Diary ---")

    keyword = input("Enter title to search: ").lower()

    if not os.path.exists(FILE_NAME):
        print("No diary entries found.")
        return

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    found = False

    for i in range(len(lines)):
        if lines[i].startswith("TITLE:"):
            if keyword in lines[i].replace("TITLE:", "").lower():
                print("\n".join(lines[i:i+3]))
                print("-" * 35)
                found = True

    if not found:
        print("Entry not found.")


def delete_all_entries():
    confirm = input("Delete ALL diary entries? (yes/no): ")

    if confirm.lower() == "yes":
        with open(FILE_NAME, "w") as file:
            file.write("")

        print("All entries deleted successfully!")
    else:
        print("Deletion cancelled.")


def main():
    if not login():
        return

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Add Diary Entry")
        print("2. View All Entries")
        print("3. Search Entry")
        print("4. Delete All Entries")
        print("5. Exit")
        print("===============================")

        choice = input("Choose option: ")

        if choice == "1":
            add_entry()

        elif choice == "2":
            view_entries()

        elif choice == "3":
            search_entry()

        elif choice == "4":
            delete_all_entries()

        elif choice == "5":
            print("\nThank you for using Personal Diary!")
            break

        else:
            print("Invalid choice! Try again.")


main()
