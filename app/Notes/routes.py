from crypt import methods
from flask import Blueprint
from .controllers import NoteCreate, NoteDetail, NoteList

notes_api = Blueprint('notes_api', __name__)

notes_api.add_url_rule(
    '/note', view_func=NoteCreate.as_view('note_create'), methods=['POST']
)

notes_api.add_url_rule(
    '/notes', view_func=NoteList.as_view('note_list'), methods=['GET']
)

notes_api.add_url_rule(
    '/note/<int:pk>', view_func=NoteDetail.as_view('note_detail'), methods=['GET', 'PATCH', 'DELETE']
)