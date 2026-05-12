from typing import Any
from fastapi.requests import Request as Request
from fastapi.responses import JSONResponse
from fastapi import FastAPI
from telebot.types import Update as Update
from telebot import TeleBot

fastapi_installed: bool

class SyncWebhookListener:
    app: FastAPI
    def __init__(self, bot: TeleBot, secret_token: str, host: str | None = '127.0.0.1', port: int | None = 443, ssl_context: tuple[Any, ...] | None = None, url_path: str | None = None) -> None: ...
    def process_update(self, request: Request, update: dict[str, Any]) -> JSONResponse: ...
    def run_app(self) -> None: ...
