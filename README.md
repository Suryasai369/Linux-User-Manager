# Linux User Manager

A Python script for managing Linux users with a user-friendly command-line interface.

## Features

- ✨ Add new users with password setup
- 🗑️ Delete existing users
- 👥 Add users to groups
- 📋 List all system users
- 🔒 Root privilege check
- 🎨 Emoji-based UI feedback

## Requirements

- Python 3.x
- Linux operating system
- Root privileges (sudo access)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/linux-user-manager.git
cd linux-user-manager
```

2. Make the script executable:
```bash
chmod +x user_manager.py
```

## Usage

Run the script with sudo privileges:

```bash
sudo ./user_manager.py
```

The script will present you with a menu of options:
1. Add a new user
2. Delete a user
3. Add user to a group
4. List all users
5. Exit

## Security Notice

⚠️ This script requires root privileges as it manages system users. Always be cautious when running scripts with elevated privileges.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.