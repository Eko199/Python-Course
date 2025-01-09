"""
Module for testing the add functionality of the Notes Application.
"""

import unittest

from app.actions.add import add
from app.actions.load_notes import load_notes
from .base_tests import BaseTestNotesApp

class TestAdd(BaseTestNotesApp):
    """Test cases for adding notes to the Notes Application."""

    def test_add_note_success(self):
        """Test adding a note successfully."""
        add("Test Note", "This is a test note.", "2023-12-31")
        notes = load_notes()
        self.assertEqual(notes["Test Note"]["content"], "This is a test note.")

    def test_add_note_no_title(self):
        """Test adding a note with no title."""
        add("", "This is a test note.", "2023-12-31")
        notes = load_notes()
        self.assertNotIn("Test Note", notes)

    def test_add_note_no_content(self):
        """Test adding a note with no content."""
        add("Test Note", "", "2023-12-31")
        notes = load_notes()
        self.assertNotIn("Test Note", notes)

    def test_add_note_already_exists(self):
        """Test adding a note that already exists."""
        add("Test Note", "This is a test note.", "2023-12-31")
        add("Test Note", "This is a test note.", "2023-12-31")
        notes = load_notes()
        self.assertEqual(len(notes), 1)

if __name__ == "__main__":
    unittest.main()
