from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Person, Activity

engine = create_engine("sqlite:///activities.db", echo=True)
sess = Session(engine)

person_1 = sess.query(Person).first()
print(person_1)

activity = person_1.activities
print(activity)

football = Activity(name="Football")

print(football.attendees)

"""
new_person = Person(first_name="Kyrian", last_name="Salas")
new_person.activities.append(football)

sess.add(new_person)
sess.commit()
"""





