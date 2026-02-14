import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from src.core.git_engine import commit_and_push
from src.logger import logger
from src.config.settings import WATCH_PATH

class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if ".git" not in event.src_path:
            logger.info(f"File changed: {event.src_path}")
            commit_and_push()

def start():
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_PATH, recursive=True)
    observer.start()
    logger.info("Watching started")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
