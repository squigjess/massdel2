import nextcord
from nextcord.ext import commands
from config import Config

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')



token = Config.DISCORD_BOT_TOKEN
bot.run(token)