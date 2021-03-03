from discord.ext.commands import MinimalHelpCommand
from discord import Embed


class Help(MinimalHelpCommand):
    """A custom help command to look prettier."""

    async def send_pages(self):
        dest = self.get_destination()

        for i, page in enumerate(self.paginator.pages):
            embed = Embed(title=f"Help | Page {i + 1}", colour=0x87CEEB)
            embed.description = page
            await dest.send(embed=embed)
