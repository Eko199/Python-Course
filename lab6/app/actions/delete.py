"""Function to delete a note."""

import json
from .load_notes import load_notes

def delete(title) -> None:
    """Delete the note with the given title."""
    notes: dict = load_notes()

    if title == "":
        print("Need title.")
    elif title not in notes:
        print("Doesn't exist, can't delete.")
    else:
        del notes[title]
        with open("notes.json", "w", encoding="utf-8") as f:
            json.dump(notes, f)
        print("Deleted.")
