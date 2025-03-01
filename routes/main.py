# routes/main.py
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from models import Scholarship, Post, db
from flask_babel import gettext as _

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    user_stage = current_user.school_stage
    scholarships = Scholarship.query.filter_by(school_stage=user_stage).all()
    # Placeholder lists for future features
    organizations = []
    internships = []
    university_recs = []
    return render_template('dashboard.html', scholarships=scholarships,
                           organizations=organizations, internships=internships, university_recs=university_recs)

'''
@main_bp.route('/posts', methods=['GET', 'POST'])
@login_required
def posts():
    if request.method == 'POST':
        content = request.form['content']
        post = Post(content=content, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash(_('Post created!'), 'success')
        return redirect(url_for('main.posts'))
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('posts.html', posts=posts)
'''
