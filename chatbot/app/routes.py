import os
import uuid
from flask import Blueprint, render_template, request, send_file, session
from chatbot.app.vertex import ask_vertex_ai
from chatbot.app.mongo import MongoHandler
from chatbot.app.vector_search import VectorSearch
from werkzeug.utils import secure_filename

main = Blueprint('main', __name__)
mongo = MongoHandler()
vector_search = VectorSearch()

@main.route('/')
def index():
    return render_template('../index.html')

@main.route('/chat', methods=['GET', 'POST'])
def chat():
    response = ''
    citations = []
    if request.method == 'POST':
        query = request.form['query']
        session_id = session.get('session_id', str(uuid.uuid4()))
        session['session_id'] = session_id

        docs = vector_search.search(query)
        response, citations = ask_vertex_ai(query, docs)

    return render_template('chat.html', response=response, citations=citations)

@main.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        for f in request.files.getlist('files'):
            filename = secure_filename(f.filename)
            path = os.path.join('uploads', filename)
            f.save(path)
            mongo.insert_uploaded_pdf(path)
    files = os.listdir('uploads')
    return render_template('upload.html', files=files)

@main.route('/sources')
def sources():
    docs = mongo.get_all_ingested()
    return render_template('sources.html', docs=docs)

@main.route('/download/<path:filename>')
def download_file(filename):
    return send_file(f'uploads/{filename}', as_attachment=True)
