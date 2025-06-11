from flask_restful import Resource

from models import Category

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
    # /categories
    # /categories/<id>
    def get(self, id=None):
        if id == None:
            categories = Category.query.all()

            return categories
        else:
            category = Category.query.filter_by(id=id).first()
            print(category)

            return category

    # /categories
    # { "name": "Travel" }
    def post(self):
        pass
