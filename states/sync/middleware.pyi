from _typeshed import Incomplete
from telebot import TeleBot as TeleBot, types as types
from telebot.handler_backends import BaseMiddleware as BaseMiddleware
from telebot.states.sync.context import StateContext as StateContext
from telebot.util import update_types as update_types

class StateMiddleware(BaseMiddleware):
    update_sensitive: bool
    update_types: Incomplete
    bot: TeleBot
    def __init__(self, bot: TeleBot) -> None: ...
    def pre_process(self, message, data) -> None: ...
    def post_process(self, message, data, exception) -> None: ...
