from dotenv import load_dotenv
from os import getenv

from src.internal import Bot

load_dotenv()

bot = Bot()

bot.load_cogs(
    "src.cogs.encodings",
)

bot.run(getenv("TOKEN"))
