import toml
from dataclasses import dataclass

conf_file = open("config.toml", "r")
config_settings = toml.loads(conf_file.read())
@dataclass
class Config:
    DISCORD_BOT_TOKEN = config_settings["DISCORD_BOT_TOKEN"]
conf_file.close()
