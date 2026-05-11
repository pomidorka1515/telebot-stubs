from _typeshed import Incomplete
from abc import ABC
from telebot import types as types, TeleBot
from telebot.async_telebot import AsyncTeleBot
from telebot.asyncio_handler_backends import State as State
from telebot.states import resolve_context as resolve_context
from typing import Any

class SimpleCustomFilter(ABC):
    key: str
    async def check(self, message: types.Message) -> Any: ...

class AdvancedCustomFilter(ABC):
    key: str
    async def check(self, message: types.Message, text: Any) -> Any: ...

class TextFilter:
    equals: str | None
    contains: list[Any] | tuple[Any] | None
    starts_with: str | list[Any] | tuple[Any] | None
    ends_with: str | list[Any] | tuple[Any] | None
    ignore_case: bool
    def __init__(self, equals: str | None = None, contains: list[Any] | tuple[Any] | None = None, starts_with: str | list[Any] | tuple[Any] | None = None, ends_with: str | list[Any] | tuple[Any] | None = None, ignore_case: bool = False) -> None: ...
    async def check(self, obj: types.Message | types.CallbackQuery | types.InlineQuery | types.Poll) -> bool: ...

class TextMatchFilter(AdvancedCustomFilter):
    key: str
    async def check(self, message: types.Message, text: Any) -> bool: ...

class TextContainsFilter(AdvancedCustomFilter):
    key: str
    async def check(self, message: types.Message, text: Any) -> bool: ...

class TextStartsFilter(AdvancedCustomFilter):
    key: str
    async def check(self, message: types.Message, text: Any) -> bool: ...

class ChatFilter(AdvancedCustomFilter):
    key: str
    async def check(self, message: types.Message | types.CallbackQuery, text: Any) -> bool: ...

class ForwardFilter(SimpleCustomFilter):
    key: str
    async def check(self, message: types.Message) -> bool: ...

class IsReplyFilter(SimpleCustomFilter):
    key: str
    async def check(self, message: types.Message | types.CallbackQuery) -> bool: ...

class LanguageFilter(AdvancedCustomFilter):
    key: str
    async def check(self, message: types.Message, text: Any) -> bool: ...

class IsAdminFilter(SimpleCustomFilter):
    key: str
    def __init__(self, bot: TeleBot | AsyncTeleBot) -> None: ...
    async def check(self, message: types.Message | types.CallbackQuery) -> bool: ...

class StateFilter(AdvancedCustomFilter):
    bot: Incomplete
    def __init__(self, bot: TeleBot | AsyncTeleBot) -> None: ...
    key: str
    async def check(self, message: types.Message, text: Any) -> bool: ...

class IsDigitFilter(SimpleCustomFilter):
    key: str
    async def check(self, message: types.Message) -> bool: ...
