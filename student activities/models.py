import sqlalchemy as db
import sqlalchemy.orm as orm

Base = orm.declarative_base()

person_activity = db.Table("person_activity", Base.metadata,
                           db.Column("id", db.Integer, primary_key=True),
                           db.Column("activity_id", db.ForeignKey("activity.id")),
                           db.Column("person_id", db.ForeignKey("person.id")),
                           db.UniqueConstraint("activity_id", "person_id"),
                           )


# Statuses

class Activity(Base):
    __tablename__ = 'activity'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)

    attendees = orm.relationship("Person", secondary=person_activity,
                                 order_by="(Person.last_name, Person.first_name)",
                                 back_populates="activities")

    def __repr__(self):
        return self.name


# Tasks

class Person(Base):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)

    activities = orm.relationship('Activity', secondary=person_activity,
                                  order_by="Activity.name",
                                  back_populates="attendees")

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'

    def greeting(self):
        print(f'{self.first_name} says hi!')
