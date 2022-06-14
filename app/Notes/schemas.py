from app.Notes.model import Notes
from ..extensions import ma

class NoteSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Notes
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)
    name = ma.String(required=True)
    frequency = ma.Float(required=True)