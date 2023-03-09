from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Person, Activity

people = [Person(first_name="Gilad", last_name="Smith"),
          Person(first_name="Daniel", last_name="Tunyan"),
          Person(first_name="Katya", last_name="Warner")]

chess = Activity(name="Chess")
fives = Activity(name="Fives")

people[0].activities.append(chess)

engine = create_engine("sqlite:///activities.db", echo=True)

with Session(engine) as sess:
    sess.add_all(people)
    sess.commit()
