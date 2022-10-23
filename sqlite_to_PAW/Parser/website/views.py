from crypt import methods
import json

from flask import Blueprint, render_template, request, flash, jsonify, redirect
from flask_login import login_required, current_user
from .models import Note
from . import db
from .parser import getPageAvito

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        # location = request.form.get('location')
        










        id = request.form.get('id')
        title = request.form.get('title')
        specific = request.form.get('specific')
        location = request.form.get('location')
        price = request.form.get('price')



        if len(title) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(
                id = id,
                title = title,
                specific = specific,
                location = location,
                price = price,
                user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


@views.route('/parse', methods=['GET', 'POST'])
def parse_avito():
    
    return redirect('/')