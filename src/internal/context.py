from discord.ext.commands import Context as _BaseContext
from discord import File
from io import StringIO


class Context(_BaseContext):
    """A Custom Context for extra functionality."""

    async def send(
        content=None,
        *,
        tts=False,
        embed=None,
        file=None,
        files=None,
        delete_after=None,
        nonce=None,
        allowed_mentions=None,
        reference=None,
        mention_author=None
    ):
        if content and len(content) > 2000 and (not file) and not files:
            file = File(StringIO(content), filename="message.txt")
            content = None
        await super().send(
            content,
            tts,
            embed,
            file,
            files,
            delete_after,
            nonce,
            allowed_mentions,
            reference,
            mention_author,
        )
