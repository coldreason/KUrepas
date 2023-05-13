from db import db
from datetime import datetime

class Currentpos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    unit_id = db.Column(db.Integer, unique=True, nullable=False)
    pos_x = db.Column(db.String(20), unique=False, nullable=False)
    pos_y = db.Column(db.String(20), unique=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def from_json(json_obj):
        currnetpos = Currentpos()
        currnetpos.unit_id = json_obj['unit_id']
        currnetpos.pos_x = json_obj['pos_x']
        currnetpos.pos_y = json_obj['pos_y']
        return currnetpos
    
    def to_json(self):
        return {
            "id": self.id,
            "unit_id": self.unit_id,
            "pos_x": self.pos_x,
            "pos_y": self.pos_y,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }