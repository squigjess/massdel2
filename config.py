import toml
from dataclasses import dataclass

conf_file = open("config.toml", "r")
config_settings = toml.loads(conf_file.read())
@dataclass
class Config:
    DISCORD_BOT_TOKEN = config_settings["DISCORD_BOT_TOKEN"]
    TEST_GUILD_IDS = config_settings["TEST_GUILD_IDS"]
    USER_TO_NUKE = config_settings["USER_TO_NUKE"]
    CHANNELS_TO_NUKE = config_settings["CHANNELS_TO_NUKE"]
conf_file.close()
