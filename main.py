from dotenv import load_dotenv
from os import getenv

from src.internal import Bot

load_dotenv()

bot = Bot()

bot.load_cogs(
    "src.cogs.encodings",
    "src.cogs.hashes",
    "src.cogs.info",
)

bot.run(getenv("TOKEN"))
