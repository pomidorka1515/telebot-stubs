from telebot import types as types
from telebot.async_telebot import AsyncTeleBot as AsyncTeleBot
from telebot.asyncio_handler_backends import BaseMiddleware as BaseMiddleware
from telebot.states.sync.context import StateContext as StateContext
from telebot.util import update_types as update_types

from typing import TypeAlias

_M: TypeAlias = types.Message | types.CallbackQuery | types.InlineQuery | types.ChosenInlineResult | types.ShippingQuery | types.PreCheckoutQuery | types.Poll | types.PollAnswer | types.ChatMemberUpdated | types.ChatJoinRequest | types.BusinessConnection | types.BusinessMessagesDeleted | types.MessageReactionUpdated | types.MessageReactionCountUpdated | types.ChatBoostUpdated | types.ChatBoostRemoved

class StateMiddleware(BaseMiddleware):
    update_sensitive: bool
    update_types: list[str]
    bot: AsyncTeleBot
    def __init__(self, bot: AsyncTeleBot) -> None: ...
    async def pre_process(self, message: _M, data: dict[str, Any]) -> None: ...
    async def post_process(self, message: _M, data: dict[str, Any], exception: BaseException | None) -> None: ...
