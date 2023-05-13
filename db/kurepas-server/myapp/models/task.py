from db import db
from datetime import datetime


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pos_s_x = db.Column(db.String(20), unique=False, nullable=False)
    pos_s_y = db.Column(db.String(20), unique=False, nullable=False)
    pos_e_x = db.Column(db.String(20), unique=False, nullable=False)
    pos_e_y = db.Column(db.String(20), unique=False, nullable=False)
    done = db.Column(db.Boolean, unique=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def from_json(json_obj):
        task = Task()
        task.pos_s_x = json_obj['pos_s_x']
        task.pos_s_y = json_obj['pos_s_y']
        task.pos_e_x = json_obj['pos_e_x']
        task.pos_e_y = json_obj['pos_e_y']
        task.done = json_obj['done']
        return task
    
    def to_json(self):
        return {
            "id": self.id,
            "pos_s_x": self.pos_s_x,
            "pos_s_y": self.pos_s_y,
            "pos_e_x": self.pos_e_x,
            "pos_e_y": self.pos_e_y,
            "done": self.done,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }