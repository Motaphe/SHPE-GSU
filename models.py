# models.py
from extensions import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)  # Remember to hash in production!
    stage = db.Column(db.String(50), nullable=False)
    preferred_language = db.Column(db.String(20), default='en')

class Scholarship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    stage = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
