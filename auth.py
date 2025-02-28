# auth.py
from flask import Blueprint, render_template, redirect, url_for, request, flash
from extensions import db
from models import User
from flask_login import login_user
from flask_babel import gettext

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            login_user(user)
            return redirect(url_for('dashboard'))
        flash(gettext('Invalid credentials.'), 'danger')
    return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        stage = request.form['stage']
        if User.query.filter_by(email=email).first():
            flash(gettext('Email already registered.'), 'danger')
            return redirect(url_for('auth.register'))
        user = User(email=email, password=password, stage=stage)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('dashboard'))
    return render_template('register.html')
