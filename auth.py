# auth.py
from flask import Blueprint, render_template, redirect, url_for, request, flash
from extensions import db
from models import User, Post, Scholarship
from flask_login import login_user, logout_user, login_required
from flask_babel import gettext
from utils.scraper import scrape_scholarships_for_stage

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            login_user(user)

            # 1. Run the scraper based on the user's stage
            stage = user.stage  # e.g., "highschool senior"
            results = scrape_scholarships_for_stage(stage)

            # 2. Store results in the DB if they're not already there
            for item in results:
                existing = Scholarship.query.filter_by(title=item['title'], stage=stage).first()
                if not existing:
                    new_sch = Scholarship(
                        title=item['title'],
                        stage=stage,
                        description=item['description']
                    )
                    db.session.add(new_sch)
            db.session.commit()

            return redirect(url_for('dashboard'))
        flash(gettext('Invalid credentials.'), 'danger')
    return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        stage = request.form.get('stage')
        if User.query.filter_by(email=email).first():
            flash(gettext('Email already registered.'), 'danger')
            return redirect(url_for('auth.register'))
        user = User(email=email, password=password, stage=stage)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('dashboard'))
    return render_template('register.html')

'''
@auth.route('/post', methods=['POST'])
@login_required
def create_post():
    content = request.form.get('content')
    if content:
        post = Post(content=content, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
    return redirect(url_for('dashboard'))
'''

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash(gettext('You have been logged out.'), 'info')
    return redirect(url_for('auth.login'))