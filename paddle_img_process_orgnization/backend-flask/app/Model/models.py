from datetime import datetime
from enum import unique

from sqlalchemy import null
from app import db



class User(db.Model):
    __tablename__ = 'User'
    userId = db.Column(db.Integer,autoincrement=True, primary_key=True)
    username = db.Column(db.String(100),unique=True)
    password = db.Column(db.String(100))
    realName = db.Column(db.String(100))
    

