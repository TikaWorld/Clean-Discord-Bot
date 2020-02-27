from discord.ext.commands import Bot

from interface import logger
from usecase.post import create_post
from usecase.user import get_user


class DiscordBot(Bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix)
        self.admin = []
        self.channel = None

    async def posting(self, message):
        new_post = await self.channel.send("set")
        content = message.content
        mention = self.user.mention
        is_secret = True
        if '!' in content[0]:
            is_secret = False
            content = content[1:]
            mention = message.author.mention
        post = create_post(new_post.id, content, get_user(message.author.id, message.author.name), is_secret)
        await new_post.edit(content=f"{mention}: {post.text}")

    async def set_admin(self, message):
        if message.author in self.admin:
            await message.channel.send("You are already Admin!")
            return
        self.admin.append(message.author)
        await message.channel.send("You are a Admin Now!")

    async def get_log(self, message):
        if message.author in self.admin:
            log = logger.get_log()
            for cont in log:
                await message.channel.send(cont)
        else:
            await message.channel.send("You can't access log!")
            return
        await message.channel.send("End Logging!")

    async def set_channel(self, message):
        if message.author in self.admin:
            self.channel = message.channel
        else:
            await message.channel.send("You can't set channel!")
            return
        await message.channel.send("Set!")