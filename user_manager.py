#!/usr/bin/env python3
import os
import subprocess
import sys
import re
import pwd
import grp
from typing import Optional, Tuple

class UserManagementError(Exception):
    """Custom exception for user management errors."""
    pass

def validate_username(username: str) -> bool:
    """
    Validate username according to Linux standards.
    - Username must be between 1 and 32 characters long
    - Username must contain only alphanumeric characters and underscores
    - Username must start with a letter or underscore
    """
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_-]{0,31}$'
    return bool(re.match(pattern, username))

def user_exists(username: str) -> bool:
    """Check if a user exists in the system."""
    try:
        pwd.getpwnam(username)
        return True
    except KeyError:
        return False

def group_exists(group: str) -> bool:
    """Check if a group exists in the system."""
    try:
        grp.getgrnam(group)
        return True
    except KeyError:
        return False

def run_command(command: list, error_msg: str) -> Tuple[bool, Optional[str]]:
    """Run a system command and handle errors."""
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, f"{error_msg}: {e.stderr}"

def check_root():
    """Ensure script runs as root."""
    if os.geteuid() != 0:
        print("❌ Please run this script as root (use sudo).")
        sys.exit(1)

def add_user() -> None:
    """Add a new user to the system with validation."""
    username = input("Enter new username: ").strip()
    
    if not username:
        print("⚠️ Username cannot be empty.")
        return
        
    if not validate_username(username):
        print("❌ Invalid username format. Username must:")
        print("  - Start with a letter or underscore")
        print("  - Contain only letters, numbers, underscores, or hyphens")
        print("  - Be between 1 and 32 characters long")
        return
        
    if user_exists(username):
        print(f"❌ User '{username}' already exists.")
        return

    success, message = run_command(
        ["useradd", "-m", username],
        f"Failed to add user '{username}'"
    )

    if success:
        print(f"✅ User '{username}' added successfully.")
        set_password = input("Do you want to set a password for this user? (y/n): ").lower()
        if set_password == "y":
            subprocess.run(["passwd", username])
    else:
        print(message)

def delete_user() -> None:
    """Delete a user from the system with validation."""
    username = input("Enter username to delete: ").strip()
    
    if not validate_username(username):
        print("❌ Invalid username format.")
        return
        
    if not user_exists(username):
        print(f"❌ User '{username}' does not exist.")
        return

    confirm = input(f"⚠️ Are you sure you want to delete '{username}'? This will also delete their home directory (y/n): ").lower()
    if confirm != "y":
        print("Operation cancelled.")
        return

    success, message = run_command(
        ["userdel", "-r", username],
        f"Failed to delete user '{username}'"
    )

    if success:
        print(f"🗑️ User '{username}' deleted successfully.")
    else:
        print(message)

def add_to_group() -> None:
    """Add a user to a group with validation."""
    username = input("Enter username: ").strip()
    if not validate_username(username):
        print("❌ Invalid username format.")
        return
        
    if not user_exists(username):
        print(f"❌ User '{username}' does not exist.")
        return

    group = input("Enter group name: ").strip()
    if not group:
        print("⚠️ Group name cannot be empty.")
        return
        
    if not group_exists(group):
        create_group = input(f"Group '{group}' does not exist. Create it? (y/n): ").lower()
        if create_group == "y":
            success, message = run_command(
                ["groupadd", group],
                f"Failed to create group '{group}'"
            )
            if not success:
                print(message)
                return
        else:
            return

    success, message = run_command(
        ["usermod", "-aG", group, username],
        f"Failed to add '{username}' to group '{group}'"
    )

    if success:
        print(f"✅ Added '{username}' to group '{group}'.")
    else:
        print(message)

def list_users() -> None:
    """List all users with additional information."""
    print("\n👥 System Users:")
    print("=" * 50)
    print(f"{'Username':<20} {'UID':<8} {'Primary Group':<15} {'Home Directory'}")
    print("-" * 50)
    
    try:
        for user in pwd.getpwall():
            if 1000 <= user.pw_uid < 65534:  # Show only regular users
                try:
                    group = grp.getgrgid(user.pw_gid).gr_name
                except KeyError:
                    group = str(user.pw_gid)
                print(f"{user.pw_name:<20} {user.pw_uid:<8} {group:<15} {user.pw_dir}")
    except Exception as e:
        print(f"❌ Error listing users: {e}")
    print("=" * 50 + "\n")

def main() -> None:
    """Main program loop with error handling."""
    try:
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

            try:
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
                    print("❌ Invalid choice, please enter a number between 1 and 5.")
            except Exception as e:
                print(f"❌ An error occurred: {str(e)}")
                
            input("\nPress Enter to continue...")

    except KeyboardInterrupt:
        print("\n👋 Program terminated by user.")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Fatal error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()