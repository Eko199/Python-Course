import asyncio
import aiohttp
import json
from typing import Any

async def getResponseJson(session: aiohttp.ClientSession, url: str, headers: dict[str, str]) -> dict[str, Any]:
    async with session.get(url, headers=headers) as response:
        return await response.json()

async def fetch(category: str, time_window: str, format: str) -> None:
    headers: dict[str, str] = { 
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhZDVhNDU4YzljZmMxODdjZThlMDdhM2ZiYTU1MjE0YyIsInN1YiI6IjY1NzRkNzA2ZTkzZTk1MDExZDRlMmM2MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.MsO7CO9573rr8rTEczZJ4PW6dnVX9xuU2OUNOcaHEts"
    }

    baseUrl: str = "https://api.themoviedb.org/3/trending/"

    async with aiohttp.ClientSession() as session:
        if category == "all":
            [tv, movies] = await asyncio.gather(getResponseJson(session, f"{baseUrl}/tv/{time_window}", headers=headers), 
                                                getResponseJson(session, f"{baseUrl}/movie/{time_window}", headers=headers))
            jsonRes: list[dict[str, Any]] = [ *tv["results"], *movies["results"] ]
        else:
            url: str = f"{baseUrl}/{category}/{time_window}"
            jsonRes: list[dict[str, Any]] = (await getResponseJson(session, url, headers))["results"]

        result: list[dict[str, float]] = sorted([
            {
                "title": r["title"] if "title" in r else r["name"], 
                "rating": r["vote_average"]
            } for r in jsonRes], 
            key=lambda r: -r["rating"])

        if format == "json":
            print(json.dumps(result))
            return
        
        print("title,rating")
        for r in result:
            print(f"{r["title"]},{r["rating"]}")