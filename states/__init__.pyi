from telebot import types as types
from typing import Any

class State:
    name: str
    group: StatesGroup
    def __init__(self) -> None: ...

class StatesGroup:
    def __init_subclass__(cls) -> None: ...
    @classmethod
    def state_list(self) -> list[Any]: ... # type: ignore
                # 
def resolve_context(
    message: 
        types.Message
        | types.CallbackQuery
        | types.BusinessConnection
        | types.BusinessMessagesDeleted
        | types.MessageReactionUpdated
        | types.MessageReactionCountUpdated
        | types.InlineQuery
        | types.ChosenInlineResult
        | types.ShippingQuery
        | types.PreCheckoutQuery
        | types.PollAnswer
        | types.ChatMemberUpdated
        | types.ChatJoinRequest
        | types.ChatBoostRemoved
        | types.ChatBoostUpdated,
    bot_id: int,
) -> tuple[int | None, int | None, str | None, int, int | None] | None: ...
