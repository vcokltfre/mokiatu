from dotenv import load_dotenv
from os import getenv

from src.internal import Bot

load_dotenv()

bot = Bot()

bot.load_cogs()

bot.run(getenv("TOKEN"))
