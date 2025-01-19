from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    # is_admin = db.Column(db.Boolean, nullable=False, default=False)  # Adjusted column

    # Relationship to Product model
    products = db.relationship('Product', backref='user', lazy=True)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    # Foreign key to User model
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# class TokenBlocklist(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     jti = db.Column(db.String(36), nullable=False, index=True)
#     created_at = db.Column(db.DateTime, nullable=False)


