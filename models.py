from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

# this allows us to define tables and their columns
metadata = MetaData()

# create a db instance
db = SQLAlchemy(metadata=metadata)

""" rules for creating models using sqlalchemy
-> must have the __tablename__ attribute
-> must have atleast one column
-> we must inherit now from db.Model
"""

""" what is the relationship btwn classes and tables
-> A whole class references a table
-> Instances of the class are rows
-> Attributes are columns
"""


class Category(db.Model, SerializerMixin):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=datetime.now())

    # will replace this with sqlalchemy_serializer
    # def to_dict(self):
    #     return {"id": self.id, "name": self.name, "created_at": self.created_at}


# /students
# class Student(db.Model):
#     pass
