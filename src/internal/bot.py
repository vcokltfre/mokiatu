from discord.ext import commands
from discord import Intents, Message

from .context import Context


class Bot(commands.Bot):
    """A subclassed version of commands.Bot with additional functionality."""

    def __init__(self, *args, **kwargs):
        intents = Intents.default()

        super().__init__(
            command_prefix=self.get_prefix, intents=intents, *args, **kwargs
        )

    def load_cogs(self, *cogs):
        """Load a list of cogs."""

        for cog in cogs:
            try:
                self.load_extension(cog)
                print(f"Cog loading: Successfully loaded {cog}")
            except Exception as e:
                print(f"Cog loading: Failed to load: {cog}\n{e}")

    async def get_prefix(self, message: Message):
        """Get a syndmic bot prefix."""

        return "."  # TODO: Add dynpref logic

    async def get_context(self, message: Message):
        return await super().get_context(message, cls=Context)
