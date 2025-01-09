"""Function to load notes from the notes.json file.""" 

import json
import os

def load_notes() -> dict:
    """Load the notes from the notes.json file, 
    or return an empty dictionary if the file does not exist or is invalid."""
    notes = None

    if os.path.exists("notes.json"):
        with open("notes.json", "r", encoding="utf-8") as f:
            try:
                notes = json.load(f)
            except json.JSONDecodeError:
                notes = {}
    else:
        notes = {}

    return notes
