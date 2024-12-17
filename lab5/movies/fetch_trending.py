import json
from typing import Any
from movies.request_handler import getJsonResult
    
def transformResult(responseRes: list[dict[str, Any]]) -> list[dict[str, float]]:
    return sorted([
        {
            "title": r["title"] if "title" in r else r["name"], 
            "rating": r["vote_average"]
        } for r in responseRes], 
        key=lambda r: -r["rating"])

def printFormatted(result:  list[dict[str, float]], format: str) -> None:
    if format == "json":
        print(json.dumps(result))
        return
    
    print("title,rating")
    for r in result:
        print(f"{r["title"]},{r["rating"]}")

async def fetch(category: str, time_window: str, format: str) -> None:
    jsonRes: list[dict[str, Any]] = await getJsonResult(category, time_window)
    result: list[dict[str, float]] = transformResult(jsonRes)
    printFormatted(result, format)
    