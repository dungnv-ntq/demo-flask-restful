from src.models.user_model import User
from src.models import db

class UserRepository():
    @staticmethod
    def find_by_id(user_id):
        user = User.query.get(user_id)
        return user
    
    @staticmethod
    def find_all():
        users = User.query.all()
        return users
    
    @staticmethod
    def create(user_name, age, address):
        user = User(user_name=user_name, age=age, address=address)
        user.save()
        return user

    @staticmethod
    def delete(user_id):
        user = User.query.get(user_id)
        user.delete()

