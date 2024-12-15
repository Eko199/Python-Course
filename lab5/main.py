import sys
import asyncio
from movies.input_validator import validate
from movies.fetch_trending import fetch

async def main():
    category, time_window, format = sys.argv[1:4]

    if not validate(category, time_window, format):
        return

    await fetch(category, time_window, format)

if __name__ == "__main__":
    asyncio.run(main())
