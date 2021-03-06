from bot_token import TOKEN
import discord
import asyncio
import logging


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'
))
logger.addHandler(handler)


class YLBotClient(discord.Client):
    async def on_ready(self):
        logger.info(f"{self.user} подключен!")
        for guild in self.guilds:
            logger.info(
                f"{self.user} подключен к чату:\n"
                f"{guild.name}(id: {guild.id})"
            )

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Привет, {member.name}!'
        )

    async def on_message(self, message):
        if message.author == self.user:
            return
        if "привет" in message.content.lower():
            await message.channel.send("И тебе привет!")
        else:
            await message.channel.send("Спасибо за сообщение")


intents = discord.Intents.default()
intents.members = True

client = YLBotClient(intents=intents)
client.run(TOKEN)
