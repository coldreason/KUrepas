from db import db
from datetime import datetime


class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, unique=False, nullable=False)
    unit_id = db.Column(db.Integer, unique=False, nullable=False)
    score = db.Column(db.Integer, unique=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def from_json(json_obj):
        score = Score()
        score.task_id = json_obj['task_id']
        score.unit_id = json_obj['unit_id']
        score.score = json_obj['score']
        return score
    
    def to_json(self):
        return {
            "id": self.id,
            "task_id": self.task_id,
            "unit_id": self.unit_id,
            "score": self.score,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }