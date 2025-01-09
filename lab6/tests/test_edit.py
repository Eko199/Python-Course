"""
Module for testing the edit functionality of the Notes Application.
"""

import unittest

from app.actions.add import add
from app.actions.load_notes import load_notes
from app.actions.edit import edit
from .base_tests import BaseTestNotesApp

class TestEdit(BaseTestNotesApp):
    """Test cases for editing notes in the Notes Application."""

    def test_edit_note_success(self):
        """Test editing a note successfully."""
        add("Test Note", "This is a test note.", "2023-12-31")
        edit("Test Note", "This is an edited note.", "2023-12-31")
        notes = load_notes()
        self.assertEqual(notes["Test Note"]["content"], "This is an edited note.")

    def test_edit_note_no_title(self):
        """Test editing a note with no title."""
        add("Test Note", "This is a test note.", "2023-12-31")
        edit("", "This is an edited note.", "2023-12-31")
        notes = load_notes()
        self.assertEqual(notes["Test Note"]["content"], "This is a test note.")

    def test_edit_note_no_content(self):
        """Test editing a note with no content."""
        add("Test Note", "This is a test note.", "2023-12-31")
        edit("Test Note", "", "2023-12-31")
        notes = load_notes()
        self.assertEqual(notes["Test Note"]["content"], "This is a test note.")

    def test_edit_note_no_changes(self):
        """Test editing a note with no changes."""
        add("Test Note", "This is a test note.", "2023-12-31")
        edit("Test Note", "", "")
        notes = load_notes()
        self.assertEqual(notes["Test Note"]["content"], "This is a test note.")

    def test_edit_note_does_not_exist(self):
        """Test editing a note that does not exist."""
        edit("Test Note", "This is an edited note.", "2023-12-31")
        notes = load_notes()
        self.assertNotIn("Test Note", notes)

if __name__ == "__main__":
    unittest.main()
