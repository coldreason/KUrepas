from db import db
from datetime import datetime

class Requestscore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, unique=False, nullable=False)
    unit_id = db.Column(db.Integer, unique=False, nullable=False)
    done = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def from_json(json_obj):
        requestscore = Requestscore()
        requestscore.task_id = int(json_obj['task_id'])
        requestscore.unit_id = int(json_obj['unit_id'])
        return requestscore
    
    def to_json(self):
        return {
            "id": self.id,
            "task_id": self.task_id,
            "unit_id": self.unit_id,
            "done": self.done,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }