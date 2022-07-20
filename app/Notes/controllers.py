from logging.handlers import DatagramHandler
from flask import request, jsonify
from flask.views import MethodView
from ..extensions import db
from ..utils.filters import filters
from .model import Notes
from .schemas import NoteSchema
from broker.main import *

class NoteList(MethodView):
    def get(self):
        schema = filters.getSchema(
            qs = request.args,
            schema_cls = NoteSchema,
            many = True
        )
        return jsonify(schema.dump(Notes.query.all())), 200

class NoteCreate(MethodView):
    def post(self):
        schema = NoteSchema()
        note = schema.load(request.json)
        note.save()
        return schema.dump(note), 201

class NoteDetail(MethodView):
    def get(self, pk):
        schema = filters.getSchema(
            qs = request.args,
            schema_cls = NoteSchema,
            many = False
        )
        note = Notes.query.filter_by(id=pk).first_or_404()
        return schema.dump(note), 200
    
    def delete(self, pk):
        note = Notes.query.filter_by(id=pk).first_or_404()
        note.delete(note)
        return {}, 204

    def patch(self, pk):
        schema = NoteSchema()
        note = Notes.query.get_or_404(pk)
        note = schema.load(request.json, instance=note, partial=True)
        note.save()
        return schema.dump(note), 200

class NoteAnalysis(MethodView):
    def get(self):
        note = Notes.query.get_or_404(read_note_id_resource()[0]["data"])
        data = read_freq_resource()
        if ((note.frequency*0.95) <= data[0]["data"]) and (data[0]["data"] <= (note.frequency*1.05)):
            return {"afinado": True,
                    "frequencia_natural_nota": note.frequency,
                    "frequencia_lida": data[0]["data"]}
        return {"afinado": False,
                "frequencia_natural_nota": note.frequency,
                "frequencia_lida": data[0]["data"]}


class WriteBroker(MethodView):
    def post(self):
        data = request.json
        if ((not "resource" in data) or (not "data" in data)):
            return {"error": "expected body with the resource and data"}, 400
        resultado = write_broker(data["resource"], data["data"])
        return {"write": resultado}, 200