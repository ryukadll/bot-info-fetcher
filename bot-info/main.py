import asyncio
import sys

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from ui.banner import print_banner
from ui.console import slow_print, divider
from core.discord_client import fetch_bot_info


def main():
    print_banner()
    input("\nPress ENTER to continue...")

    divider()
    slow_print("Enter your Discord bot token:")
    token = input("> ").strip()

    divider()
    slow_print("Validating token and fetching bot information...\n", 0.03)

    bot_info = asyncio.run(fetch_bot_info(token))

    if not bot_info:
        slow_print("Invalid bot token.", 0.03)
        return

    slow_print("Bot authenticated successfully.\n", 0.03)

    divider()
    slow_print(f"Bot Username : {bot_info['username']}")
    slow_print(f"Bot ID       : {bot_info['id']}")
    slow_print(f"Server Count : {len(bot_info['guilds'])}")

    divider()
    slow_print("Servers:\n", 0.03)

    for name, guild_id in bot_info["guilds"]:
        slow_print(f"• {name} | ID: {guild_id}", 0.01)

    divider()
    slow_print("Done.", 0.02)


if __name__ == "__main__":
    main()
