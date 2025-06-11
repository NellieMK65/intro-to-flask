# import the flask package
from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from models import db
from resources.entry import EntryResource

# initialize our app
app = Flask(__name__)

# configuring our flask app through the config object
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notebook.db"

# link flask-restful with flask
api = Api(app)

# create a migrate object to manage migrations
migrate = Migrate(app, db)

# link our db to the flask app
db.init_app(app)


# GET "/"
@app.route("/", methods=["POST"])  # decorator -> modify our functions
def index():
    return {"message": "Welcome to my first flask app"}


# C.R.U.D

# CREATE -> POST -> /categories
# READ -> GET -> All categories -> /categories
# READ -> GET -> Single category -> /categories/<id> (UPDATE -> PATCH), (DELETE)


# Create a single category
@app.post("/categories")
def create_category():
    return {"message": "Category created"}


# Retrieves all categories
@app.get("/categories")
def get_categories():
    return []


# Retrieve a single catgory
@app.get("/categories/<id>")
def get_category(id):
    return {}


# Update a single catgory
@app.patch("/categories/<id>")
def update_category(id):
    return {"message": "Category updated"}


# Retrieve a single catgory
@app.delete("/categories/<id>")
def delete_category(id):
    return {"message": "Category deleted"}


# Create/Identify resources


# flask-restful -> OOP
# class Index(Resource):

#     def get():
#         return {"message": "Welcome to my first flask app"}

#     def post():
#         pass

#     def patch():
#         pass

#     def delete():
#         pass


# app.add_resource("/", Index)

api.add_resource(EntryResource, "/entries", "/entries/<entry_id>")
