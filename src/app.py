from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from src.models import db, ma
from src.config import get_config
from src.resources.user_resource import UserResousrce, UserListResource


app = Flask(__name__)
app.config.from_object(get_config())
migrate = Migrate(app, db)
db.init_app(app)
ma.init_app(app)


# api
api = Api(app)
api.add_resource(UserResousrce, '/api/users/<id>')
api.add_resource(UserListResource, '/api/users')


@app.route("/")
def hello():
    return 'hello world'
