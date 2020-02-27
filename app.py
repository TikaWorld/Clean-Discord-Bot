import os

from bot import make_bot

bot = make_bot()
token = os.getenv("DISCORD_TOKEN")
password = os.getenv("DISCORD_PASSWORD")

bot.run(token)
