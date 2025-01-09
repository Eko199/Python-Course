"""Function to list all notes."""
from .load_notes import load_notes

def list_notes() -> None:
    """List all notes."""
    notes:dict = load_notes()

    print("Listing notes...")
    if len(notes) == 0:
        print("Nothing to list.")
    else:
        for title in notes:
            #FIXED BUG: notes[title]["due_date"]
            print("- " + title + " (Due: " + (notes[title]["due_date"]
                                              if "due_date" in notes[title]
                                              else "None") + ")")
