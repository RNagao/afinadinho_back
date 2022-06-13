from ..extensions import db
from ..base_model import BaseModel


class Notes(BaseModel):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), nullable = False)
    frequency = db.Column(db.Integer, nullable = False)
    instrument = db.Column(db.String(64), nullable = False, default)