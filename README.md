# Linux User Manager

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Python script for managing Linux users with a user-friendly command-line interface. Features enhanced security, input validation, and comprehensive error handling.

## Features

- ✨ Add new users with password setup
- 🗑️ Delete existing users
- 👥 Add users to groups
- 📋 List all system users
- 🔒 Root privilege check
- 🎨 Emoji-based UI feedback

## Requirements

- Python 3.6 or higher
- Linux operating system
- Root privileges (sudo access)

## Features in Detail

- ✨ **User Creation**
  - Validates username format
  - Checks for existing users
  - Optional password setup
  - Creates home directory automatically

- 🗑️ **User Deletion**
  - Safety confirmation prompt
  - Removes user's home directory
  - Validates user existence

- 👥 **Group Management**
  - Add users to existing groups
  - Create new groups on demand
  - Validates group existence

- 📋 **User Listing**
  - Shows username and UID
  - Displays primary group
  - Shows home directory location
  - Filters system users

- 🛡️ **Security Features**
  - Root privilege verification
  - Input validation
  - Error handling
  - Safe command execution

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Suryasai369/linux-user-manager.git
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

## Development

### Setting up Development Environment

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/linux-user-manager.git
cd linux-user-manager
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install development dependencies:
```bash
pip install black pytest pytest-cov
```

### Running Tests

Run the test suite:
```bash
python -m pytest test_user_manager.py -v
```

Run tests with coverage:
```bash
python -m pytest test_user_manager.py --cov=user_manager
```

### Code Style

This project uses the Black code formatter. To format your code:
```bash
black user_manager.py test_user_manager.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Format your code with Black (`black .`)
4. Run the tests (`python -m pytest`)
5. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
6. Push to the branch (`git push origin feature/AmazingFeature`)
7. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.