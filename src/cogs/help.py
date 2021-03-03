from discord.ext import commands

from src.internal import Bot


class Help(commands.Cog):
    """The help command."""

    def __init__(self, bot: Bot):
        self.bot = bot
        self.bot.all_commands["help"].cog = self


def setup(bot: Bot):
    bot.add_cog(Help(bot))
