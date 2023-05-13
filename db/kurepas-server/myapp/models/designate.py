from db import db
from datetime import datetime

class Designate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, unique=True, nullable=False)
    unit_id = db.Column(db.Integer, unique=False, nullable=False)
    score = db.Column(db.Integer, unique=False, nullable=False)
    done = db.Column(db.Boolean, unique=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def from_json(json_obj):
        designate = Designate()
        designate.id = json_obj['id']
        designate.task_id = json_obj['task_id']
        designate.unit_id = json_obj['unit_id']
        designate.score = json_obj['score']
        designate.done = json_obj['done']
        return designate
    
    def to_json(self):
        return {
            "id": self.id,
            "task_id": self.task_id,
            "unit_id": self.unit_id,
            "score": self.score,
            "done": self.done,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }