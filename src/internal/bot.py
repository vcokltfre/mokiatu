from discord.ext import commands
from discord import Intents, Message


class Bot(commands.Bot):
    """A subclassed version of commands.Bot with additional functionality."""

    def __init__(self, *args, **kwargs):
        intents = Intents.default()

        super().__init__(
            command_prefix=self.get_prefix,
            intents=intents,
            *args,
            **kwargs
        )

    def load_cogs(self, *cogs):
        """Load a list of cogs."""

        for cog in cogs:
            try:
                self.load_extension(cog)
                print(f"Cog loading: Successfully loaded {cog}")
            except Exception as e:
                print(f"Cog loading: Failed to load: {cog}")

    async def get_prefix(self, message: Message):
        """Get a syndmic bot prefix."""

        return "." # TODO: Add dynpref logic
