"""
Module for testing the delete functionality of the Notes Application.
"""

import unittest

from app.actions.add import add
from app.actions.delete import delete
from app.actions.load_notes import load_notes
from .base_tests import BaseTestNotesApp

class TestNotesApplicaiton(BaseTestNotesApp):
    """Test cases for deleting notes in the Notes Application."""

    def test_delete_note_success(self):
        """Test deleting a note successfully."""
        add("Test Note", "This is a test note.", "2023-12-31")
        delete("Test Note")
        notes = load_notes()
        self.assertNotIn("Test Note", notes)

    def test_delete_note_does_not_exist(self):
        """Test deleting a note that does not exist."""
        delete("Test Note")
        notes = load_notes()
        self.assertNotIn("Test Note", notes)

if __name__ == "__main__":
    unittest.main()
