# Linux User Manager Documentation

## Overview
The Linux User Manager is a command-line tool designed to simplify user management tasks on Linux systems. It provides an intuitive interface for common user management operations with enhanced security features and input validation.

## Features Documentation

### User Creation
The user creation feature includes:
- Username format validation
- Automatic home directory creation
- Optional password setup
- Duplicate username checks

### User Deletion
The deletion process includes:
- User existence verification
- Confirmation prompt for safety
- Home directory cleanup
- Error handling for system-critical users

### Group Management
Group management features:
- Add users to existing groups
- Create new groups on demand
- Group existence validation
- Error handling for invalid operations

### User Listing
The listing functionality shows:
- Username
- User ID (UID)
- Primary group
- Home directory location
- Filters out system users

## Security Features

1. Root Privilege Check
   - Ensures the script runs with appropriate permissions
   - Prevents unauthorized access

2. Input Validation
   - Username format validation
   - Group name validation
   - Command injection prevention

3. Error Handling
   - Graceful error recovery
   - User-friendly error messages
   - System command execution safety

## Best Practices

When using the Linux User Manager:
1. Always run with sudo privileges
2. Review changes before confirming
3. Backup important user data before deletion
4. Use strong passwords when creating new users
5. Be cautious with group permissions

## Troubleshooting

Common issues and solutions:
1. Permission Denied
   - Ensure you're running with sudo
   - Check file permissions

2. Invalid Username
   - Usernames must start with a letter or underscore
   - Only use alphanumeric characters, underscores, or hyphens
   - Keep username length between 1 and 32 characters

3. Group Operations Failed
   - Verify group exists
   - Check for typos in group names
   - Ensure user exists before adding to group