#!/usr/bin/env python3
import os
import subprocess
import sys

def check_root():
    """Ensure script runs as root."""
    if os.geteuid() != 0:
        print("❌ Please run this script as root (use sudo).")
        sys.exit(1)

def add_user():
    username = input("Enter new username: ").strip()
    if not username:
        print("⚠️ Username cannot be empty.")
        return
    try:
        subprocess.run(["useradd", "-m", username], check=True)
        print(f"✅ User '{username}' added successfully.")
        set_password = input("Do you want to set a password for this user? (y/n): ").lower()
        if set_password == "y":
            subprocess.run(["passwd", username])
    except subprocess.CalledProcessError:
        print(f"❌ Failed to add user '{username}'.")

def delete_user():
    username = input("Enter username to delete: ").strip()
    confirm = input(f"Are you sure you want to delete '{username}'? (y/n): ").lower()
    if confirm != "y":
        return
    try:
        subprocess.run(["userdel", "-r", username], check=True)
        print(f"🗑️ User '{username}' deleted successfully.")
    except subprocess.CalledProcessError:
        print(f"❌ Failed to delete user '{username}'.")

def add_to_group():
    username = input("Enter username: ").strip()
    group = input("Enter group name: ").strip()
    try:
        subprocess.run(["usermod", "-aG", group, username], check=True)
        print(f"✅ Added '{username}' to group '{group}'.")
    except subprocess.CalledProcessError:
        print(f"❌ Could not add '{username}' to group '{group}'.")

def list_users():
    print("\n👥 List of users:")
    subprocess.run(["cut", "-d:", "-f1", "/etc/passwd"])
    print()

def main():
    check_root()
    
    while True:
        print("""
====================================
        🧑‍💻 User Management Menu
====================================
1. Add a new user
2. Delete a user
3. Add user to a group
4. List all users
5. Exit
""")
        choice = input("Enter your choice [1-5]: ").strip()

        if choice == "1":
            add_user()
        elif choice == "2":
            delete_user()
        elif choice == "3":
            add_to_group()
        elif choice == "4":
            list_users()
        elif choice == "5":
            print("👋 Exiting program.")
            sys.exit(0)
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()