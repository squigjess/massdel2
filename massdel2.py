import nextcord
from nextcord.ext import commands
from config import Config

bot = commands.Bot()

def is_me(m): # Predicate that checks if a given message is written by me
    return m.author.id == Config.USER_TO_NUKE and m.channel.id in Config.CHANNELS_TO_NUKE

def run_by_me(m):
    return m.user.id != Config.USER_TO_NUKE

msg_list = []

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(description="Count all messages by the defined user in this channel", dm_permission=False, guild_ids=Config.TEST_GUILD_IDS)
async def confirm(interaction: nextcord.Interaction):
    if run_by_me(interaction):
        await interaction.send("Not the authorised user.", ephemeral=True)
        return None

    print(f"---------------\nCounting all messages by user @{interaction.user.name} in channel #{interaction.channel.name}")
    count = 0
    async for msg in interaction.channel.history(limit=None).filter(is_me):
        print(msg)
        count += 1
    print(f"\nDone! Found {count} messages.")

@bot.slash_command(description="Purge all messages from the defined user in this channel", dm_permission=False, guild_ids=Config.TEST_GUILD_IDS)
async def purge(interaction: nextcord.Interaction):
    if run_by_me(interaction)
        await interaction.send("Not the authorised user.", ephemeral=True)
        return None


    print(f"---------------\nDeleting all messages by user @{interaction.user.name} in channel #{interaction.channel.name}")
    count = 0
    async for msg in interaction.channel.history(limit=None).filter(is_me):
        await msg.delete()
        count += 1
        print(f"Deleted {count} messages...")
    print(f"\nDone! Found {count} messages. Deleted some of them?")

@bot.slash_command(description="Find all messages and save to a list for later deletion", dm_permission=False, guild_ids=Config.TEST_GUILD_IDS)
async def compile(interaction: nextcord.Interaction):
    if run_by_me(interaction)
        await interaction.send("Not the authorised user.", ephemeral=True)
        return None

    print(f"---------------\nFinding all messages by user @{interaction.user.name} in channel #{interaction.channel.name}")
    count = 0
    async for msg in interaction.channel.history(limit=None).filter(is_me):
        msg_list.append(msg)
        count += 1
        print(f"Found {count} messages...")
    print(f"Compiled a list of {len(msg_list)} messages...")

@bot.slash_command(description="Deletes all messages saved with /compile", dm_permission=False, guild_ids=Config.TEST_GUILD_IDS)
async def delete_compiled(interaction: nextcord.Interaction):
    if run_by_me(interaction)
        await interaction.send("Not the authorised user.", ephemeral=True)
        return None

    print(f"---------------\nDeleting {len(msg_list)} messages")
    count = 0
    for msg in msg_list:
        await msg.delete()
        count += 1
        print(count)
    print(f"Deleted (?) {len(msg_list)} messages...")


token = Config.DISCORD_BOT_TOKEN
bot.run(token)