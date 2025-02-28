# routes/chat.py
from flask import Blueprint, render_template
from flask_login import login_required
from flask_socketio import send
from app import socketio

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat')
@login_required
def chat():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)
