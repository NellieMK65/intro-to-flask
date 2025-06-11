from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy

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


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.TIMESTAMP)
