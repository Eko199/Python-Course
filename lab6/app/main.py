"""Command-line Note-Taking Application"""

import argparse
from json import JSONDecodeError
from actions.add import add
from actions.view import view
from actions.delete import delete
from actions.list_notes import list_notes
from actions.edit import edit

def main():
    """Main function for the command-line note-taking application"""

    try:
        parser = argparse.ArgumentParser(description="Command-line Note-Taking Application")
        parser.add_argument("action",
                            choices=["add", "view", "delete", "list", "edit"],
                            help="What do you want to do?")
        parser.add_argument("--title", help="Title of the note")
        parser.add_argument("--content", help="Content of the note (only for `add` action)")
        parser.add_argument("--due-date", help="Optional due date (only for `add` action)")
        args = parser.parse_args()

        if args.action == "add":
            if args.title is None:
                print("Need title.")
            elif args.content is None:
                print("Needs content.")
            else:
                add(args.title, args.content, args.due_date)
        elif args.action == "view":
            view(args.title)
        elif args.action == "delete":
            delete(args.title)
        elif args.action == "list":
            list_notes()
        elif args.action == "edit":
            edit(args.title, args.content, args.due_date)
        else:
            print("Invalid action.")
    except (OSError, JSONDecodeError, AttributeError, argparse.ArgumentError) as e:
        print(e)

if __name__ == "__main__":
    main()
