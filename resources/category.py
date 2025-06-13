from flask import request, jsonify
from flask_restful import Resource, reqparse

from models import Category, db

"""
-> Every time we create a resource we have to inherit from the Resource class imported from
flask_restful
-> We define our methods(instance) using http verbs/methods(get, post, delete)
"""

# /categories -> resource/path
# http://localhost:5000/categories -> get, post
# http -> protocal
# localhost:5000 -> domain
# /categories, /categories/id -> resource


class CategoryResource(Resource):
    # create the validation method as a class instance so that it can be reused in both post and patch
    parser = reqparse.RequestParser()
    parser.add_argument("name", required=True, help="Category name is required")

    # /categories
    # /categories/<id>
    def get(self, id=None):
        if id is None:
            categories = Category.query.all()

            return jsonify([category.to_dict() for category in categories])
        else:
            category = Category.query.filter_by(id=id).first()

            if category is None:
                return {"message": "Category not found"}, 404

            return jsonify(category.to_dict())

    # /categories
    # { "name": "Travel" }
    def post(self):
        # data = request.get_json()
        data = self.parser.parse_args()

        category = Category(**data)

        db.session.add(category)
        db.session.commit()

        return {"message": "Category added successfully"}, 201

    def patch(self, id):
        data = self.parser.parse_args()

        # retrieve the record
        category = Category.query.filter_by(id=id).first()

        if category is None:
            return {"message": "Category not found"}, 404

        # update instance with new values
        category.name = data["name"]

        # commit to db
        db.session.commit()

        return {"message": "Category updated successfully"}

    # only admins can delete categories
    def delete(self, id):
        # retrieve the record
        category = Category.query.filter_by(id=id).first()

        if category is None:
            return {"message": "Category not found"}, 404

        db.session.delete(category)

        db.session.commit()

        return {"message": "Category deleted successfully"}
