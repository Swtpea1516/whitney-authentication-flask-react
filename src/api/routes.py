

from flask import Flask, request, jsonify, Blueprint
from api.models import db, User
from api.utils import APIException
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

api = Blueprint('api', __name__)

@api.route('/signup', methods=['POST'])
def signup():
    body = request.get_json()
    if "email" not in body or "password" not in body:
        raise APIException("Please provide both email and password", status_code=400)

    email = body['email']
    password = body['password']

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify(message="User already exists"), 400

    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(message="Successfully created user"), 200

@api.route('/login', methods=['POST'])
def login():
    body = request.get_json()
    if "email" not in body or "password" not in body:
        raise APIException("Please provide both email and password", status_code=400)

    email = body['email']
    password = body['password']

    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify(message="Wrong email or password"), 401

@api.route('/user', methods=['GET'])
@jwt_required()
def get_user():
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user).first()

    if user:
        return jsonify(user.serialize()), 200
    else:
        return jsonify(message="User not found"), 404

@api.route('/logout', methods=['POST'])
@jwt_required()
def logout():
   
    return jsonify(message="Logged out successfully"), 200












# from flask import Flask, request, jsonify, url_for, Blueprint
# from api.models import db, User 
# from api.utils import generate_sitemap, APIException
# from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
# from werkzeug.security import generate_password_hash, check_password_hash
# from datetime import datetime, timedelta

# api = Blueprint('api', __name__)

# @api.route('/hello', methods=['POST', 'GET'])
# def handle_hello():
#     response_body = {
#         "message": "Hello! I'm a message that came from the backend, check the network tab on the Google inspector, and you will see the GET request"
#     }
#     return jsonify(response_body), 200

# @api.route('/signup', methods=['POST'])
# def signup():
#     body = request.get_json(force=True)
#     user=User()
#     if"email"not in body:
#         raise APIException("Please put email",status_code=400)
#     if"password"not in body:
#         raise APIException("Please put password",status_code=400)
#     user.email = body['email']  
#     user.password = body['password']  
#     user.is_active=True
  
    
    
#     existing_user = User.query.filter_by(email=user.email).first()
#     if existing_user:
#         return jsonify("User already exists"), 400

#     hashed_password = generate_password_hash(user.password, method='sha256')
#     user = User(email=user.email, password=hashed_password)
#     db.session.add(user)
#     db.session.commit()
#     return jsonify("Successfully created user"),200

# @api.route('/login', methods=['GET'])
# @jwt_required()
# def login():
#     body = request.get_json(force=True)
#     email = body['email']
#     password = body['password']  


    
#     user = User.query.filter_by(email=email).first()
    
#     if user and check_password_hash(user.password, password):
    
#         access_token = create_access_token(identity=email)
#         return jsonify(access_token=access_token)
#     else:
#         return jsonify("Wrong email or password")

# # @api.route('/user', methods=['GET'])
# # @jwt_required()
# # def get_user():
#     current_user = get_jwt_identity()
# #     user = User.query.filter_by(email=current_user).first()

#     if user:
#         return jsonify(user.serialize()), 200
#     else:
#         return jsonify({"message": "User not found"}), 404

# @api.route('/logout', methods=['DELETE'])
# @jwt_required()
# def validate_identity():
#     current_user = get_jwt_identity()
#     return jsonify(logged_in_as=current_user)

#  log out ?




























# from flask import Flask, request, jsonify, url_for, Blueprint
# from api.models import db, User
# from api.utils import generate_sitemap, APIException
# import hashlib
# from flask_jwt_extended import create_access_token
# from flask_jwt_extended import get_jwt_identity
# from flask_jwt_extended import jwt_required
# from werkzeug.security import generate_password_hash, check_password_hash
# from datetime import datetime, timedelta

# api = Blueprint('api', __name__)


# @api.route('/hello', methods=['POST', 'GET'])
# def handle_hello():
#     response_body = {
#         "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
#     }
#     return jsonify(response_body), 200

# @api.route('/signup', methods=['POST'])
# def signup():
#     body=request.get_json(force=True)
#     email = body('email')
#     password = body('password')
#     has_email=User.query.filter_by(email=email).first()
#     if has_email is None:
#         hashed_password = generate_password_hash(password, method='sha256')
#         new_user = User(email=email, password=hashed_password)
#         db.session.add(new_user)
#         db.session.commit()
#         return jsonify("successfully created user")
#     else:
#         return jsonify("user already exists"), 400

# @api.route('/login', methods=['POST'])
# def login():
#     body = request.get_json ( force = True)
#     email = body['email']
#     password =generate_password_hash(password, method='sha256')
#     print(password)
#     has_user = User.query.filter_by(email = email, password = password).first()
#     if has_user is not None:
#         access_token = create_access_token(identity = email)
#         return jsonify(access_token = access_token)
#     else: 
#         return jsonify("Wrong email or password")


# @api.route('/user', methods=['GET'])
# @jwt_required()
# def get_user():
#     id = get_jwt_identity()
#     user = User.query.filter_by(id=id).first()

#     if user is not None:
#         return jsonify(user.serialize()), 200

#     return jsonify({"message": "Uh-oh"}), 400

# @api.route('/logout', methods=['GET'])
# @jwt_required()
# def validate_identity():
#     current_user = get_jwt_identity()
#     return jsonify(logged_in_as = current_user)






