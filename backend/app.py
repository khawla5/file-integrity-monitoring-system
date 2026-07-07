from flask import Flask, jsonify
from flask_cors import CORS
from database import Session, FileRecord

app = Flask(__name__)
CORS(app)

@app.route("/files")
def files():
    session = Session()
    records = session.query(FileRecord).all()
    session.close()

    return jsonify([
        {"path": record.path, "hash": record.hash}
        for record in records
    ])

if __name__ == "__main__":
    app.run(debug=True)