from bot_token import TOKEN
import discord
import asyncio


client = discord.Client()


@client.event
async def on_ready():
    print(f"{client.user} подключен!")
    for guild in client.guilds:
        print(
            f"{client.user} подключен к чату:\n"
            f"{guild.name}(id: {guild.id})"
        )


client.run(TOKEN)
