# telebot-stubs
Stub `.pyi` files for pyTelegramBotApi.  
A live copy of this repo is available at:  
https://pomi.lol/static/other/telebot-stubs/  
Note that it includes unstaged changes.  
## Philosophy
These stubs mirror **the actual source code** of telebot, not the Telegram Bot API specification.   
- If the library declares `chat_id: int`, the stub uses `int`, even though the Bot API accepts `int | str`.  
- If a docstring says "returns a response object" but the code returns a string, the stub types what the code actually does.  
  
## Limitations  
- Some parameters that the Bot API supports may be missing because the library hasn't implemented them.  
- Some types may be narrower than the Bot API spec (e.g., `chat_id: int` where the API allows strings).  
## Status
Incomplete, working on it  
## License
GPL-3.0  
