import os
import discord

from interface import logger
from interface.discord import DiscordBot


def make_bot():
    bot = DiscordBot("/")
    bot.add_listener(on_ready)
    bot.add_listener(on_message)
    return bot


async def on_ready():
    print("Ready!")


async def on_message(message):
    if message.author == bot.user:
        return
    if type(message.channel) == discord.TextChannel:
        if message.content == f"!set channel":
            await bot.set_channel(message)

    if type(message.channel) == discord.DMChannel:
        if message.content == f"!login":
            await bot.set_admin(message)
        elif message.content == f"!log":
            await bot.get_log(message)
        else:
            await bot.posting(message)


bot = make_bot()
token = os.getenv("DISCORD_TOKEN")
password = os.getenv("DISCORD_PASSWORD")

bot.run(token)
