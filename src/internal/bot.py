from discord.ext import commands
from discord import Intents, Message, Game
import logging

from .context import Context
from .help import Help

FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(format=FORMAT)


class Bot(commands.Bot):
    """A subclassed version of commands.Bot with additional functionality."""

    def __init__(self, *args, **kwargs):
        self.logger = logging.getLogger("mokiatu.core")
        self.logger.setLevel(logging.INFO)

        self.logger.info("Starting up...")

        intents = Intents.default()

        super().__init__(
            command_prefix='.',
            intents=intents,
            help_command=Help(),
            activity=Game(name=".help"),
            *args,
            **kwargs,
        )

    def load_cogs(self, *cogs):
        """Load a list of cogs."""

        for cog in cogs:
            try:
                self.load_extension(cog)
                self.logger.info(f"Successfully loaded cog {cog}")
            except Exception as e:
                self.logger.error(f"Failed to load cog {cog}", exc_info=True)

        self.logger.info("Cog loading finished.")

    async def get_context(self, message: Message):
        return await super().get_context(message, cls=Context)
