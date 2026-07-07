import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from hash_utils import calculate_hash
from database import Session, FileRecord

WATCH_FOLDER = "../important-files"

class Handler(FileSystemEventHandler):

    def on_modified(self, event):
        if event.is_directory:
            return

        print("⚠ File modified:", event.src_path)

        session = Session()
        path = event.src_path
        new_hash = calculate_hash(path)

        record = session.query(FileRecord).filter_by(path=path).first()

        if record and record.hash != new_hash:
            print("🚨 ALERT: File changed!", path)
            record.hash = new_hash
            session.commit()

observer = Observer()
observer.schedule(Handler(), WATCH_FOLDER, recursive=True)
observer.start()

print("👀 Watching files in real-time...")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()