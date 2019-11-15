import uuid
from src import db


class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    stars = db.Column(db.String(120), nullable=False)


class Table:
    def __init__(self, number, guests_count):
        self.number = number
        self.guest_count = guests_count
        self.id = str(uuid.uuid4())


