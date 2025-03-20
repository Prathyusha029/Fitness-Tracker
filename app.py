from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from flask import jsonify
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.getcwd(), 'fitness.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Define the User loader function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Define User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    hash = db.Column(db.String(150), nullable=False)
    workouts = db.relationship('Workout', backref='user', lazy=True)
    water_intakes = db.relationship('WaterIntake', backref='user', lazy=True)

# Define Workout model
class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Define WaterIntake model
class WaterIntake(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@app.before_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user:
            flash('Username already taken. Please choose a different username.', 'danger')
            return render_template('register.html')

        try:
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = User(username=username, hash=hashed_password)
            db.session.add(new_user)
            db.session.commit()

            flash('Registration successful!', 'success')
            return redirect(url_for('login'))

        except Exception as e:
            flash(f'Registration failed: {str(e)}', 'danger')
            return render_template('register.html')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.hash, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Login unsuccessful. Please check your username and password.', 'danger')

    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    workouts = current_user.workouts
    water_intakes = current_user.water_intakes
    return render_template('dashboard.html', workouts=workouts, water_intakes=water_intakes)

@app.route('/log_workout', methods=['POST'])
@login_required
def log_workout():
    if request.method == 'POST':
        data = request.get_json()
        workout_type = data.get('type')
        duration = data.get('duration')

        if not workout_type or not duration:
            return jsonify({'error': 'Missing required fields'}), 400

        try:
            workout = Workout(type=workout_type, duration=duration, date=datetime.now(), user_id=current_user.id)
            db.session.add(workout)
            db.session.commit()
            return jsonify({'message': 'Workout logged successfully', 'duration': duration}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

@app.route('/log_water', methods=['POST'])
@login_required
def log_water():
    if request.method == 'POST':
        amount = request.json.get('amount')

        if not amount:
            return jsonify({'error': 'Amount is required.'}), 400

        try:
            water_intake = WaterIntake(amount=amount, date=datetime.now(), user_id=current_user.id)
            db.session.add(water_intake)
            db.session.commit()
            return jsonify({'message': 'Water intake logged successfully', 'amount': amount}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

@app.route('/get_logs', methods=['GET'])
@login_required
def get_logs():
    workouts = Workout.query.filter_by(user_id=current_user.id).all()
    water_intakes = WaterIntake.query.filter_by(user_id=current_user.id).all()

    workout_data = [{"type": w.type, "duration": w.duration, "date": w.date} for w in workouts]
    water_data = [{"amount": w.amount, "date": w.date} for w in water_intakes]

    return jsonify({"workouts": workout_data, "water_intakes": water_data})

if __name__ == '__main__':
    app.run(debug=True)
