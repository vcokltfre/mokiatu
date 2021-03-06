from discord.ext.commands import Context as _BaseContext
from discord import File
from io import StringIO
from time import time


class Context(_BaseContext):
    """A Custom Context for extra functionality."""

    def __init__(self, *args, **kwargs):
        self.start_invoke = time()
        super().__init__(*args, **kwargs)

    async def send(
        self,
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
        if content and len(content) > 2000 and not (file or files):
            file = File(StringIO(content), filename="message.txt")
            content = None
        await super().send(
            content=content,
            tts=tts,
            embed=embed,
            file=file,
            files=files,
            delete_after=delete_after,
            nonce=nonce,
            allowed_mentions=allowed_mentions,
            reference=reference,
            mention_author=mention_author,
        )
