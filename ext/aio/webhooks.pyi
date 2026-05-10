from _typeshed import Incomplete
from fastapi.requests import Request as Request
from telebot.types import Update as Update

fastapi_installed: bool

class AsyncWebhookListener:
    app: Incomplete
    def __init__(self, bot, secret_token: str, host: str | None = '127.0.0.1', port: int | None = 443, ssl_context: tuple | None = None, url_path: str | None = None) -> None: ...
    async def process_update(self, request: Request, update: dict): ...
    async def run_app(self) -> None: ...
