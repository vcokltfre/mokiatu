from discord.ext import commands
from base64 import b64encode, b64decode
from hashlib import sha256

from src.internal import Bot


class Encodings(commands.Cog):
    """A set of text encoding commands."""

    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.group(name="encode")
    async def encode(self, ctx: commands.Context):
        """A group of commands for encoding text."""
        pass

    @encode.command(name="base64", aliases=["b64"])
    async def encode_b64(self, ctx: commands.Context, *, text: str):
        """Encode text using base64 encoding."""
        output = b64encode(text.encode('utf-8'))

        await ctx.send(output.decode())

    @commands.group(name="decode")
    async def decode(self, ctx: commands.Context):
        """A group of commands for decoding text."""
        pass

    @decode.command(name="base64", aliases=["b64"])
    async def decode_b64(self, ctx: commands.Context, *, text: str):
        """Decode Base64 encoded text."""
        output = b64decode(text.encode())

        await ctx.send(output.decode())


def setup(bot: Bot):
    bot.add_cog(Encodings(bot))
