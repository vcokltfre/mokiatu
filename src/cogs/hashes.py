from discord.ext import commands
from discord import Embed
from hashlib import sha256, sha512, md5, new, algorithms_available

from src.internal import Bot


class Hashes(commands.Cog):
    """A set of text hashing commands."""

    def __init__(self, bot: Bot):
        self.bot = bot

    @staticmethod
    def build_embed(hash_type: str, input: str, output, note: str = None) -> Embed:
        embed = Embed(title=f"Hash: {hash_type}", colour=0x87CEEB, description=f"**Input:**\n```\n{input}```")
        embed.add_field(name="Result:", value=f"```\n{output.hexdigest()}```", inline=False)
        embed.add_field(name="Block Size:", value=str(output.block_size), inline=True)
        embed.add_field(name="Digest Size:", value=str(output.digest_size), inline=True)
        if note:
            embed.add_field(name="Note:", value=note, inline=False)
        return embed

    @commands.command(name="sha256")
    async def hash_sha256(self, ctx: commands.Context, *, text: str):
        """Hash text using SHA256."""
        output = sha256(text.encode("utf-8"))

        await ctx.send(embed=self.build_embed("SHA256", text, output))

    @commands.command(name="sha512")
    async def hash_sha512(self, ctx: commands.Context, *, text: str):
        """Hash text using SHA512."""
        output = sha512(text.encode("utf-8"))

        await ctx.send(embed=self.build_embed("SHA512", text, output))

    @commands.command(name="md5")
    async def hash_md5(self, ctx: commands.Context, *, text: str):
        """Hash text using MD5. [Insecure]"""
        output = md5(text.encode("utf-8"))

        await ctx.send(embed=self.build_embed("MD5", text, output, "MD5 is an insecure hash algorithm with known vulnerabilities and collisions."))

    @commands.command(name="hash")
    async def hash_sha512(self, ctx: commands.Context, name: str = None, *, text: str = None):
        """Hash text using a user provided hash."""
        try:
            h = new(name, text.encode("utf-8"))
        except Exception as e:
            hashes_help = "Available hashes: " + ", ".join(sorted(algorithms_available))
            return await ctx.send("No hashing algorithm found by that name!\n" + hashes_help)

        await ctx.send(embed=self.build_embed(name, text, h))

    @commands.command(name="hashes")
    async def hashes(self, ctx: commands.Context):
        """Get a list of hashes supported by Mokiatu."""
        embed = Embed(title="Available Hashes", colour=0x87CEEB)

        for command in self.walk_commands():
            if command.name == "hashes": continue
            embed.add_field(name=command.name, value=command.help, inline=False)

        embed.set_footer(text="Use .hash <hash> for more specific hashes like ripemd160")

        await ctx.send(embed=embed)


def setup(bot: Bot):
    bot.add_cog(Hashes(bot))
