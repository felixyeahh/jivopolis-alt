from . import (
    callback,
    admin_commands,
    inline_bot,
    on_photo_sent,
    start,
    stickers_handler,
    emoji_handler,
)
from .. import Dispatcher


async def register_all(dp: Dispatcher) -> None:
    """
    function to register all bot hadlers

    handlers:
        - callback
        - inline bot
        - photo handler
        - start command
        - stickers handler
        - commands for admins
    """
    start.register(dp)
    from . import payments
    callback.register(dp)
    admin_commands.register(dp)
    inline_bot.register(dp)
    on_photo_sent.register(dp)
    stickers_handler.register(dp)
    emoji_handler.register(dp)
    from . import new_member_handler
    from . import message_handlers
    return (new_member_handler, message_handlers, payments)
