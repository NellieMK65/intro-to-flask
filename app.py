import os

# import the flask package
from flask import Flask
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

from models import db
from resources.entry import EntryResource
from resources.category import CategoryResource
from resources.user import SingInResource, LoginResource

# imports the configs stored inside the .env file
load_dotenv()

# initialize our app
app = Flask(__name__)


# configuring our flask app through the config object
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notebook.db"
# allow sqlalchemy to display generate sql on the terminal
app.config["SQLALCHEMY_ECHO"] = True
# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET")  # Change this!

jwt = JWTManager(app)

# link our flask app with the encryption package
bcrypt = Bcrypt(app)

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

# We have refactored the category routes to use flask-restful

# # Create a single category
# @app.post("/categories")
# def create_category():
#     return {"message": "Category created"}


# Retrieves all categories
# @app.get("/categories")
# def get_categories():
#     return []


# Retrieve a single catgory
# @app.get("/categories/<id>")
# def get_category(id):
#     return {}


# Update a single catgory
# @app.patch("/categories/<id>")
# def update_category(id):
#     return {"message": "Category updated"}


# Retrieve a single catgory
# @app.delete("/categories/<id>")
# def delete_category(id):
#     return {"message": "Category deleted"}


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


# http://localhost:5000/login -> { "email": "jane@gmail.com", "password": "12345" } -> POST
class Login(Resource):
    def post(self):
        return {"message": "Login successful"}
        # user = User.query.filter_by(email = 'jane@gmail.com').first()

        # if user == None:
        #     return { "message": "Invalid email/password" }


api.add_resource(EntryResource, "/entries", "/entries/<entry_id>")
api.add_resource(CategoryResource, "/categories", "/categories/<int:id>")
api.add_resource(SingInResource, "/signin")
api.add_resource(LoginResource, "/login")
