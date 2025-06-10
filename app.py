# import the flask package
from flask import Flask
# from flask_restful import Resource, Api

# initialize our app
app = Flask(__name__)

# api = Api(app)


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
