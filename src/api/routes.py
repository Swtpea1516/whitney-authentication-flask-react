from flask import Flask, request, jsonify, url_for, Blueprint, render_template, flash, redirect
from flask_login import LoginManager, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from api.models import db, User
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)

login_manager = LoginManager()
login_manager.login_view = "api.login" 

@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():
    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }
    return jsonify(response_body), 200

@api.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Signup successful. Please login.')
        return redirect(url_for('api.login'))
    return render_template('signup.html')

@api.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('api.private'))
        flash('Invalid credentials. Please try again.')
    return render_template('login.html')

@api.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('api.login'))

@api.route('/private')
@login_required
def private():
    return "This is the private dashboard. You are authenticated."

