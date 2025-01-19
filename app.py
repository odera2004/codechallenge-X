from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db
from flask_jwt_extended import JWTManager
from datetime import timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Long.db'

db.init_app(app)
migrate = Migrate(app, db)

app.config["JWT_SECRET_KEY"] = "vghsdvvsjvy436u4wu37118gcd#"  
app.config["JWT_ACCESS_TOKEN_EXPIRES"] =  timedelta(hours=1)
jwt = JWTManager(app)
jwt.init_app(app)


from views import *

app.register_blueprint(product_bp)
app.register_blueprint(user_bp)
app.register_blueprint(auth_bp)

# @jwt.token_in_blocklist_loader
# def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
#     jti = jwt_payload["jti"]
#     token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()

#     return token is not None