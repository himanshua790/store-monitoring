from app import db


class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.String(20), unique=True, nullable=False)
    status = db.Column(db.String(10), nullable=False)
    timestamp_utc = db.Column(db.DateTime, nullable=False)

    def __init__(self, store_id, status, timestamp_utc):
        self.store_id = store_id
        self.status = status
        self.timestamp_utc = timestamp_utc

    def __repr__(self):
        return f"Store(id={self.id}, store_id={self.store_id}, status={self.status}, timestamp_utc={self.timestamp_utc})"


db.create_all()  # Run this to create tables
