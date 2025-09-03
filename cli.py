from helpers import (
    create_team, list_teams, delete_team,
    create_locker, list_lockers, update_locker, delete_locker,
    search_locker, exit_program
)

def menu():
    print("\n--- Sports Locker CLI ---")
    print("1. Create team")
    print("2. List teams")
    print("3. Delete team")
    print("4. Create locker")
    print("5. List lockers")
    print("6. Update locker")
    print("7. Delete locker")
    print("8. Search locker by player name")
    print("0. Exit")

def main():
    while True:
        menu()
        choice = input("> ").strip()
        if choice == "1": create_team()
        elif choice == "2": list_teams()
        elif choice == "3": delete_team()
        elif choice == "4": create_locker()
        elif choice == "5": list_lockers()
        elif choice == "6": update_locker()
        elif choice == "7": delete_locker()
        elif choice == "8": search_locker()
        elif choice == "0": exit_program()
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()
