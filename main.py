import discord
import os
from discord import app_commands


class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f'Logged in as {self.user}.')


client = aclient()
tree = app_commands.CommandTree(client)


@tree.command(name='ping', description="test response")
async def self(interaction: discord.Interaction, name: str):
    await interaction.response.send_message(f'Hello {name}!')
client.run('')
