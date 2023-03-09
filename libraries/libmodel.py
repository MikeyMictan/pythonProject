import sqlalchemy as db
import sqlalchemy.orm as orm

Base = orm.declarative_base()

book_author = db.Table("book_author", Base.metadata,
                           db.Column("id", db.Integer, primary_key=True),
                           db.Column("book_id", db.ForeignKey("book.id")),
                           db.Column("author_id", db.ForeignKey("author.id")),
                           db.UniqueConstraint("book_id", "author_id"),
                           )


# Statuses

class Book(Base):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, unique=True, nullable=False)
    ISBN_number = db.Column(db.Integer, unique=True, nullable=False)
    num_pages = db.Column(db.Integer, unique=True, nullable=False)
    publication_date = db.Column(db.String, unique=True, nullable=False)
    publisher_id = db.Column(db.Integer, unique=True, nullable=False)
    
    authors = orm.relationship("Author", secondary=book_author,
                                 order_by="(Author.last_name, Author.first_name)",
                                 back_populates="books")

    def __repr__(self):
        return self.title


# Tasks

class Author(Base):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_name = db.Column(db.String, nullable=False)

    books = orm.relationship('Book', secondary=book_author,
                                  order_by="Book.name",
                                  back_populates="authors")

    def __repr__(self):
        return self.author_name


class publisher(Base):
    __tablename__ = 'publisher'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    publisher_name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return self.publisher_name


