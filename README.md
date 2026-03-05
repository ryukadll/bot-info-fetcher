# Bot Info


![standard](https://github.com/user-attachments/assets/bf7e6fd4-3593-4e4b-9a94-30b710bb2562)


A lightweight command-line tool to validate a Discord bot token and display information about the bot — including its username, ID, and all servers it's currently in.

---

## Features

- Validates a Discord bot token via the official Discord API
- Fetches the bot's username, discriminator, and ID
- Lists all servers (guilds) the bot is a member of
- Styled terminal output with animated text and colour gradients (via `pystyle`)

---

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`:
  - [`discord.py`](https://pypi.org/project/discord.py/)
  - [`pystyle`](https://pypi.org/project/pystyle/)

> **Note:** `aiohttp` is used internally for async HTTP requests to the Discord API.

---

## Installation

```bash
# Clone the repository
git clone https://github.com/ryukadll/bot-info-fetcher.git
cd bot-info

# Install dependencies
pip install -r requirements.txt
```

---

## Usage

```bash
python main.py
```

You will be prompted to enter your Discord bot token. The tool will then:

1. Validate the token against the Discord API
2. Display the bot's username and ID
3. List every server the bot is currently in

### Example Output

```
──────────────────────────────────────────────────────────
Bot Username : MyBot#1234
Bot ID       : 123456789012345678
Server Count : 3
──────────────────────────────────────────────────────────
Servers:

• My Cool Server     | ID: 111111111111111111
• Another Server     | ID: 222222222222222222
• Testing Ground     | ID: 333333333333333333
──────────────────────────────────────────────────────────
Done.
```

---

## Project Structure

```
bot-info/
├── main.py                  # Entry point
├── requirements.txt         # Python dependencies
├── core/
│   ├── __init__.py
│   └── discord_client.py    # Discord API logic (token validation, guild fetching)
└── ui/
    ├── __init__.py
    ├── banner.py            # ASCII art banner
    └── console.py           # Styled print helpers (slow_print, divider)
```

---

## Security Notice

- **Never share your bot token.** Treat it like a password.
- This tool only reads bot information — it does not modify any Discord data.
- Tokens are entered at runtime and are not stored or logged anywhere.

---

## License

This project is licensed with MIT. 
