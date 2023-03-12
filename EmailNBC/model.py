import sqlalchemy as db
from sqlalchemy.orm import declarative_base, validates
import re

Base = declarative_base()
class EmailAddress(Base):
    __tablename__ = 'Emails'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return self.email


@validates('email')
def validate_email(self, key, address):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.fullmatch(pattern, address):
        raise ValueError('Invalid email address')
    if key != 'email':
        raise ValueError('Key must be "email"')
    return address

