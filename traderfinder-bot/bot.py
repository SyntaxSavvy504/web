import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

class TraderBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='!', intents=intents)
        
    async def setup_hook(self):
        await self.load_extension('cogs.analysis')
        await self.load_extension('cogs.signals')
        await self.load_extension('cogs.utilities')

bot = TraderBot()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')

if __name__ == '__main__':
    bot.run(os.getenv('DISCORD_TOKEN'))
