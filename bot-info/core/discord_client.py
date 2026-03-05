import aiohttp
import asyncio

DISCORD_API = "https://discord.com/api/v10"


async def fetch_bot_info(token: str):
    headers = {
        "Authorization": f"Bot {token}"
    }

    timeout = aiohttp.ClientTimeout(total=15)

    async with aiohttp.ClientSession(headers=headers, timeout=timeout) as session:
        async with session.get(f"{DISCORD_API}/users/@me") as response:
            if response.status != 200:
                return None
            user = await response.json()

        async with session.get(f"{DISCORD_API}/users/@me/guilds") as response:
            if response.status != 200:
                guilds = []
            else:
                guilds = await response.json()

    return {
        "username": f"{user['username']}#{user['discriminator']}",
        "id": user["id"],
        "guilds": [(g["name"], g["id"]) for g in guilds],
    }
