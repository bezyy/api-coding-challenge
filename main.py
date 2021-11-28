from flask import Flask
from flask_restful import Api, Resource
import datetime

app = Flask(__name__)
api = Api(app)

users = {}


class User(Resource):
    def post(self, id, password):
        users[id] = {"password": password, "mood": {}}
        return users[id]


class Mood(Resource):
    def post(self, id, mood):
        x = datetime.datetime.now()
        users[id]["mood"][str(x.date())] = mood
        return users[id]

    def get(self, id):
        return users[id]["mood"] + "\n"


api.add_resource(User, "/user/<string:id>/<string:password>")
api.add_resource(Mood, "/mood/<string:id>/<string:mood>")


if __name__ == "__main__":
    app.run(debug=True)
