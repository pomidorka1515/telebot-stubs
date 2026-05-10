from _typeshed import Incomplete
from telebot import types as types
from telebot.async_telebot import AsyncTeleBot as AsyncTeleBot
from telebot.asyncio_handler_backends import BaseMiddleware as BaseMiddleware
from telebot.states.sync.context import StateContext as StateContext
from telebot.util import update_types as update_types

class StateMiddleware(BaseMiddleware):
    update_sensitive: bool
    update_types: Incomplete
    bot: AsyncTeleBot
    def __init__(self, bot: AsyncTeleBot) -> None: ...
    async def pre_process(self, message, data) -> None: ...
    async def post_process(self, message, data, exception) -> None: ...
