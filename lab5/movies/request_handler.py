import aiohttp
import asyncio
from typing import Any

async def getResponseJson(session: aiohttp.ClientSession, url: str, headers: dict[str, str]) -> dict[str, Any]:
    async with session.get(url, headers=headers) as response:
        return await response.json()

async def getJsonResult(category: str, time_window: str) -> list[dict[str, Any]]:
    headers: dict[str, str] = { 
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhZDVhNDU4YzljZmMxODdjZThlMDdhM2ZiYTU1MjE0YyIsInN1YiI6IjY1NzRkNzA2ZTkzZTk1MDExZDRlMmM2MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.MsO7CO9573rr8rTEczZJ4PW6dnVX9xuU2OUNOcaHEts"
    }

    baseUrl: str = "https://api.themoviedb.org/3/trending/"
    async with aiohttp.ClientSession() as session:
        if category == "all":
            [tv, movies] = await asyncio.gather(getResponseJson(session, f"{baseUrl}/tv/{time_window}", headers=headers), 
                                                getResponseJson(session, f"{baseUrl}/movie/{time_window}", headers=headers))
            return [ *tv["results"], *movies["results"] ]
        
        url: str = f"{baseUrl}/{category}/{time_window}"
        return (await getResponseJson(session, url, headers))["results"]