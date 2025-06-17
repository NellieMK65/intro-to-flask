from flask_restful import Resource, reqparse
from flask_bcrypt import generate_password_hash, check_password_hash
from models import db, User


class SingInResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("full_name", required=True)
    parser.add_argument("email", required=True)
    parser.add_argument("password", required=True, help="Password is required")

    def post(self):
        data = self.parser.parse_args()

        # check if the user has an account
        email = User.query.filter_by(email=data["email"]).first()

        if email:
            return {"message": "Email address is already taken"}, 422

        # 2 .encrypt the password
        hash = generate_password_hash(data["password"]).decode("utf-8")

        # 3. save the user
        user = User(full_name=data["full_name"], email=data["email"], password=hash)

        db.session.add(user)
        db.session.commit()

        return {"message": "account created successfully", "access_token": ""}, 201


class LoginResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "email", required=True, type=str, help="Email address is required"
    )
    parser.add_argument(
        "password", required=True, type=str, help="Password is required"
    )

    def post(self):
        data = self.parser.parse_args()

        # 1. check if user with email is present
        user = User.query.filter_by(email=data["email"]).first()

        if user is None:
            return {"message": "Incorrect email address/password"}, 401

        # 2. verify password
        if check_password_hash(user.password, data["password"]):
            access_token = ""

            return {
                "message": "Login successful",
                "user": user.to_dict(),
                "access_token": access_token,
            }, 201
        else:
            return {"message": "Incorrect email or password"}, 401
