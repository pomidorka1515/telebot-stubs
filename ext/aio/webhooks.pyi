from typing import Any
from fastapi.requests import Request as Request
from fastapi import FastAPI
from telebot.types import Update as Update
from telebot.async_telebot import AsyncTeleBot
fastapi_installed: bool

class AsyncWebhookListener:
    app: FastAPI
    def __init__(self, bot: AsyncTeleBot, secret_token: str, host: str | None = '127.0.0.1', port: int | None = 443, ssl_context: tuple[..., Any] | None = None, url_path: str | None = None) -> None: ...
    async def process_update(self, request: Request, update: dict[str, Any]): ...
    async def run_app(self) -> None: ...
