#!/usr/bin/env python3
import unittest
import sys
from unittest.mock import patch, MagicMock
from user_manager import validate_username, user_exists, group_exists

class TestUserManager(unittest.TestCase):
    """Test cases for Linux User Manager script."""

    def test_username_validation(self):
        """Test username validation function."""
        # Valid usernames
        self.assertTrue(validate_username("user123"))
        self.assertTrue(validate_username("_user123"))
        self.assertTrue(validate_username("user_name"))
        self.assertTrue(validate_username("u"))
        
        # Invalid usernames
        self.assertFalse(validate_username(""))  # Empty
        self.assertFalse(validate_username("123user"))  # Starts with number
        self.assertFalse(validate_username("user@123"))  # Special character
        self.assertFalse(validate_username("a" * 33))  # Too long

    @patch('pwd.getpwnam')
    def test_user_exists(self, mock_getpwnam):
        """Test user existence check."""
        # Test existing user
        mock_getpwnam.return_value = MagicMock()
        self.assertTrue(user_exists("existinguser"))
        
        # Test non-existing user
        mock_getpwnam.side_effect = KeyError()
        self.assertFalse(user_exists("nonexistentuser"))

    @patch('grp.getgrnam')
    def test_group_exists(self, mock_getgrnam):
        """Test group existence check."""
        # Test existing group
        mock_getgrnam.return_value = MagicMock()
        self.assertTrue(group_exists("existinggroup"))
        
        # Test non-existing group
        mock_getgrnam.side_effect = KeyError()
        self.assertFalse(group_exists("nonexistentgroup"))

if __name__ == '__main__':
    unittest.main()