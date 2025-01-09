"""Function to add a new note."""

import json
from .load_notes import load_notes

def add(title, content, due_date) -> None:
    """Add a new note with the given title, content, and optional due date."""

    notes: dict = load_notes()

    if title == "":
        print("No title, can't add note.")
    elif content == "":
        print("No content, can't add note.")
    else:
        if title in notes:
            print("Already exists, won't overwrite.")
        else:
            if due_date:
                notes[title] = {
                    "content": content,
                    "due_date": due_date
                }
            else:
                notes[title] = {
                    "content": content,
                }

            with open("notes.json", "w", encoding="utf-8") as f:
                f.write(json.dumps(notes))

            print("Added new note", title)
