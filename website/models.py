from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.column(db.String(10000))
    date = db.column(db.DateTime(timezone= True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class UserModel(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable= False)
    firstName = db.Column(db.String(150))
    passeword = db.Column(db.String(150))
    notes = db.relationshp('Note')
    
