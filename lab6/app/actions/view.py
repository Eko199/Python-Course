"""Function to view a note."""

from .load_notes import load_notes

def view(title) -> None:
    """View the note with the given title."""
    notes: dict = load_notes()

    if title == "":
        print("Need title.")
    elif title not in notes:
        print("Doesn't exist.")
    else:
        print(title)
        print("---")
        print(notes[title]["content"])
        print("---")
        #FIXED BUG: notes[title]["due_date"]
        if "due_date" in notes[title]:
            print("Due:" + notes[title]["due_date"])
        else:
            print("No due date.")
