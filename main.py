from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import datetime

app = Flask(__name__)
api = Api(app)

mood_post_args = reqparse.RequestParser()

users = {}


class User(Resource):
    def post(self, id, password):
        users[id] = {"password": password, "mood": {},
                     "streak": 0, "next_update": "0000-00-00"}
        return users[id]


class Mood(Resource):
    def post(self, id):
        mood = request.form['mood']
        x = datetime.datetime.now()

        # check if user submitted mood rating 1 day ago
        if (str(x.date) == users[id]["next_update"]):
            users[id]["streak"] += 1

        next_update = x + datetime.timedelta(days=1)
        users[id]["next_update"] = str(next_update.date())
        users[id]["mood"][str(x.date())] = mood
        return users[id]

    def get(self, id):
        return users[id]["mood"]


api.add_resource(User, "/user/<string:id>/<string:password>")
api.add_resource(Mood, "/mood/<string:id>")


if __name__ == "__main__":
    app.run(debug=True)
