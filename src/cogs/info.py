from discord.ext import commands
from discord import Embed
from os import walk
from json import loads

from src.internal import Bot


class Info(commands.Cog):
    """Get info about a specific thing related to cryptography."""

    def __init__(self, bot: Bot):
        self.bot = bot
        self.items = {}
        self.load()

    @staticmethod
    def loadfile(filename: str):
        with open(filename) as f:
            return f.read()

    def load(self):
        for root, dirs, files in walk("./static/info"):
            for file in files:
                if not file.endswith(".json"):
                    continue
                data = loads(self.loadfile(f"{root}/{file}"))
                item = {}

                for name, value in data.items():
                    if isinstance(value, str) and value.startswith("$$"):
                        item[name] = self.loadfile(f"./static/info/{value[2:]}")
                    else:
                        item[name] = value

                item["color"] = 0x87CEEB
                self.items[file[:-5]] = item

    @commands.command(name="info")
    async def info(self, ctx: commands.Context, *, item: str = None):
        if item is None or item.lower() not in self.items:
            embed = Embed(
                title="Information", colour=0x87CEEB, description="Info snippets:"
            )
            for name in sorted(i for i in self.items):
                embed.description += f"\n{name}"
            return await ctx.send(embed=embed)

        await ctx.send(embed=Embed.from_dict(self.items[item.lower()]))


def setup(bot: Bot):
    bot.add_cog(Info(bot))
