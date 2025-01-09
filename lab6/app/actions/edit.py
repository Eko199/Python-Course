"""Function to edit a note."""

import json
from .load_notes import load_notes

def edit(title, content, due_date) -> None:
    """Edit the note with the given title, changing the content and/or due date"""

    notes: dict = load_notes()

    if not title or title == "":
        print("Need title.")
    elif title not in notes:
        print(f"Note with title {title} does not exist.")
    elif (not content or content == "") and (not due_date or due_date == ""):
        print("No content or due date provided - no changes made to the note.")
    else:
        if content and content != "":
            notes[title]["content"] = content

        if due_date == "none":
            del notes[title]["due_date"]
        elif due_date and due_date != "":
            notes[title]["due_date"] = due_date

        with open("notes.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(notes))

        print("Note successfully edited.")
