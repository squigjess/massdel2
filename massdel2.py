import nextcord
from nextcord.ext import commands
from config import Config

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(description="foo.", dm_permission=False, guild_ids=Config.TEST_GUILD_IDS)
async def confirm(interaction: nextcord.Interaction):
    await interaction.send("bar", ephemeral=True)


token = Config.DISCORD_BOT_TOKEN
bot.run(token)