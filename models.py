from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):  # Inherit UserMixin
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    user_name = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)  # Store hashed password
    is_family_member = db.Column(db.Boolean, default=False)
    relation = db.Column(db.String(255), nullable=True)
    is_financer = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def set_password(self, password):
        """Hashes password before saving."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Checks if entered password matches the stored hash."""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.user_name}>"
    

class PersonalAccount(db.Model):
    __tablename__ = 'personal_account'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    transaction_with = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)  # New field
    source = db.Column(db.String(255), nullable=True)  # New field
    debited_amount = db.Column(db.String(255), nullable=True)
    credited_amount = db.Column(db.String(255), nullable=True)
    total_balance = db.Column(db.String(255), nullable=False)
    date_and_time = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship with User model
    user = db.relationship('User', foreign_keys=[user_id], backref=db.backref('accounts', lazy=True))
    transaction_user = db.relationship('User', foreign_keys=[transaction_with], backref=db.backref('transactions', lazy=True))

    def __repr__(self):
        return f"<PersonalAccount User ID: {self.user_id}, Balance: {self.total_balance}, Source: {self.source}>"


