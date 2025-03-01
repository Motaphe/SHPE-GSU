# app.py
from flask import Flask, render_template, redirect, url_for, request, flash, session
from config import Config
from extensions import db  # Import the db instance from extensions
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_babel import Babel, gettext
from auth import auth as auth_blueprint  # Import the auth blueprint

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
babel = Babel(app)

# Register the blueprint with a URL prefix if desired
app.register_blueprint(auth_blueprint, url_prefix='/auth')

# Import models after initializing db to avoid circular import issues
with app.app_context():
    from models import User, Scholarship, Post, Organization, Event, Internship, UniversityPrep, Vote, Comment

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.context_processor
def inject_get_locale():
    return dict(get_locale=get_locale)

def get_locale():
    return session.get('lang', request.accept_languages.best_match(['en', 'es', 'ind']))

babel.locale_selector_func = get_locale

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Simplified – hash passwords in production!
        email = request.form['email']
        password = request.form['password']
        stage = request.form.get('school_stage')
        language = request.form.get('language', 'en')
        if User.query.filter_by(email=email).first():
            flash(gettext('Email already registered.'), 'danger')
            return redirect(url_for('register'))
        user = User(email=email, password=password, stage=stage, preferred_language=language)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        session['lang'] = language
        return redirect(url_for('dashboard'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email, password=password).first()  # Use proper password hashing!
        if user:
            login_user(user)
            session['lang'] = user.preferred_language
            return redirect(url_for('dashboard'))
        flash(gettext('Invalid credentials.'), 'danger')
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    user_stage = current_user.stage
    scholarships = Scholarship.query.filter_by(stage=user_stage).all()
    organizations = Organization.query.filter_by(stage=user_stage).all()
    events = Event.query.filter_by(stage=user_stage).all()
    internships = Internship.query.filter_by(stage=user_stage).all()
    university_preps = UniversityPrep.query.all()  # add filtering based on location/majors if needed

    return render_template('dashboard.html',
                           scholarships=scholarships,
                           organizations=organizations,
                           events=events,
                           internships=internships,
                           university_preps=university_preps)


@app.route('/set_language/<lang>')
def set_language(lang):
    session['lang'] = lang
    return redirect(request.referrer or url_for('dashboard'))

# Optional: endpoints for community posts, messaging, etc.

if __name__ == '__main__':
    app.run(debug=True)
