# routes/auth.py
from flask import Blueprint, render_template, redirect, url_for, request, flash
from models import db, User
from flask_login import login_user, logout_user
from flask_babel import gettext as _

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']  # In production, hash this!
        school_stage = request.form['school_stage']
        preferred_language = request.form.get('preferred_language', 'en')
        user = User(email=email, password=password, school_stage=school_stage, preferred_language=preferred_language)
        db.session.add(user)
        db.session.commit()
        flash(_('Registration successful. Please log in.'), 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email, password=password).first()  # In production, verify the hashed password!
        if user:
            login_user(user)
            flash(_('Logged in successfully.'), 'success')
            return redirect(url_for('main.dashboard'))
        else:
            flash(_('Invalid email or password.'), 'danger')
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    logout_user()
    flash(_('You have been logged out.'), 'info')
    return redirect(url_for('main.index'))
