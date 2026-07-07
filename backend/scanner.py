import os
from hash_utils import calculate_hash
from database import Session, FileRecord

WATCH_FOLDER = "../important-files"

def scan_files():
    session = Session()

    for root, dirs, files in os.walk(WATCH_FOLDER):
        for file in files:
            path = os.path.join(root, file)
            file_hash = calculate_hash(path)

            record = session.query(FileRecord).filter_by(path=path).first()

            if record:
                if record.hash != file_hash:
                    print("⚠ FILE CHANGED:", path)
                    record.hash = file_hash
            else:
                print("NEW FILE:", path)
                session.add(FileRecord(path=path, hash=file_hash))

    session.commit()
    session.close()

scan_files()