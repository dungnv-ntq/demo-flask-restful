from flask import request
from flask_restful import Resource
import json

from src.repositories.user_repository import UserRepository
from src.models.user_model import UserSchema

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class UserResousrce(Resource):
    def get(self, id: int):
        user = UserRepository.find_by_id(id)
        return user_schema.dump(user), 200

    def delete(self, id: int):
        UserRepository.delete(id)
        return "successful", 200


class UserListResource(Resource):
    def get(self):
        users = UserRepository.find_all()
        return users_schema.dump(users), 200
    
    def post(self):
        request_json = request.get_json(silent=True)
        user_name = request_json.get('user_name')
        age = request_json.get('age')
        address = request_json.get('address')

        user = UserRepository.create(user_name, age, address)
        return user_schema.dump(user), 200
