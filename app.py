from flask import Flask
from flask_restful import Api, Resource, reqparse
from main import lab1, lab2, lab3

app = Flask(__name__)
api = Api(app)

list_mapping = {}


class ListView(Resource):

    def get(self, id=None):
        if id is None:
            return list_mapping, 200
        if id not in list_mapping:
            return "List not found", 404
        return list_mapping[id], 200

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("action")
        args = parser.parse_args()

        action = args.get('action')

        if action == 'create':
            if id in list_mapping:
                return "List already exists", 201
            else:
                list_mapping[id] = []
                return "List created", 200
        elif action == 'lab1':
            if id not in list_mapping:
                return "List not found", 404
            return lab1(list_mapping[id])
        elif action == 'lab2':
            if id not in list_mapping:
                return "List not found", 404
            return lab2(list_mapping[id])
        elif action == 'lab3':
            if id not in list_mapping:
                return "List not found", 404
            return lab3(list_mapping[id])
        else:
            return "Action not found", 404

    def put(self, id=None):
        if id is None:
            return "Please, specify list id", 422
        if id not in list_mapping:
            return "List not found", 404

        parser = reqparse.RequestParser()
        parser.add_argument("element")
        args = parser.parse_args()

        try:
            element = int(args.get("element"))
        except ValueError:
            return "Only integer element supported", 442

        list_mapping[id].append(element)
        return list_mapping[id], 200

    def delete(self, id=None):
        if id is None:
            return "Please, specify list id", 422
        if id not in list_mapping:
            return "List not found", 404
        return list_mapping.pop(id), 200


api.add_resource(ListView, "/list/", "/list/<string:id>")

app.run()
