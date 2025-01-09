"""
Base test class for the Notes Application.
"""

import unittest

class BaseTestNotesApp(unittest.TestCase):
    """Base test class for Notes Application that handles file work."""

    def setUp(self):
        with open("notes.json", "r", encoding="utf-8") as file:
            self.initial_content = file.read()

        with open("notes.json", "w", encoding="utf-8") as file:
            file.write("")

    def tearDown(self):
        with open("notes.json", "w", encoding="utf-8") as file:
            file.write(self.initial_content)
