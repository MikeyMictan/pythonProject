from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model import EmailAddress

engine = create_engine("sqlite:///emails.sqlite", echo=True)
sess = Session(engine)

new_email = EmailAddress(email="mictan0910@highgateschool.org.uk")

sess.add(new_email)
sess.commit()
