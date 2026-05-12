from watchdog.events import FileSystemEvent as FileSystemEvent, FileSystemEventHandler
from logging import Logger

logger: Logger

class EventHandler(FileSystemEventHandler):
    def on_any_event(self, event: FileSystemEvent) -> None: ...

def restart_file() -> None: ...
