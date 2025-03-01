# models.py
from extensions import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    stage = db.Column(db.String(50), nullable=False)
    preferred_language = db.Column(db.String(20), default='en')

class Scholarship(db.Model):
    __tablename__ = 'scholarships'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    stage = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
    votes = db.relationship('Vote', backref='post', lazy=True)
    comments = db.relationship('Comment', backref='post', lazy=True)

class Organization(db.Model):
    __tablename__ = 'organizations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    stage = db.Column(db.String(50), nullable=False)  # which stage is it relevant to?
    description = db.Column(db.Text)

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    stage = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100))
    date = db.Column(db.Date)
    description = db.Column(db.Text)

class Internship(db.Model):
    __tablename__ = 'internships'
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(150), nullable=False)
    stage = db.Column(db.String(50), nullable=False)
    field = db.Column(db.String(100))
    description = db.Column(db.Text)

class UniversityPrep(db.Model):
    __tablename__ = 'university_preps'
    id = db.Column(db.Integer, primary_key=True)
    university = db.Column(db.String(150), nullable=False)
    support_network = db.Column(db.Boolean, default=False)
    location = db.Column(db.String(100))
    majors = db.Column(db.String(200))  # comma-separated majors or use a relation
    advice = db.Column(db.Text)

class Vote(db.Model):
    __tablename__ = 'votes'
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
