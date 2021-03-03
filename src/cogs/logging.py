from discord.ext import commands
from time import time

from src.internal import Bot


class Logging(commands.Cog):
    """Event logging for Mokiatu."""

    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_completion(self, ctx: commands.Context):
        """Log successfull command invokations."""

        self.bot.logger.info(f"Command '{ctx.command}' run by {ctx.author} in {ctx.guild or 'DMs'} ({ctx.author.id} in {ctx.channel.id}) | Took {round((time() - ctx.start_invoke) * 1000, 3)}ms")



def setup(bot: Bot):
    bot.add_cog(Logging(bot))
