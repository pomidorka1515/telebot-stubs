from typing import TypeAlias, Any
from telebot import TeleBot as TeleBot, types as types
from telebot.handler_backends import BaseMiddleware as BaseMiddleware
from telebot.states.sync.context import StateContext as StateContext
from telebot.util import update_types as update_types

_M: TypeAlias = types.Message | types.CallbackQuery | types.InlineQuery | types.ChosenInlineResult | types.ShippingQuery | types.PreCheckoutQuery | types.Poll | types.PollAnswer | types.ChatMemberUpdated | types.ChatJoinRequest | types.BusinessConnection | types.BusinessMessagesDeleted | types.MessageReactionUpdated | types.MessageReactionCountUpdated | types.ChatBoostUpdated | types.ChatBoostRemoved

class StateMiddleware(BaseMiddleware):
    update_sensitive: bool
    update_types: list[int]
    bot: TeleBot
    def __init__(self, bot: TeleBot) -> None: ...
    def pre_process(self, message: _M, data: dict[str, Any]) -> None: ...
    def post_process(self, message: _M, data: dict[str, Any], exception: BaseException | None) -> None: ...
