from flask import Flask, request, jsonify, json

users = [
    {"id": 1, "name": "John", "age": 24},
    {"id": 2, "name": "Alex", "age": 52},
    {"id": 3, "name": "Amy",  "age": 27},
]


def find(lst, key, value):
    for i, dic in enumerate(lst):
        if dic[key] == value:
            return i
    return -1


api = Flask(__name__)


@api.route('/')
def index():
    return jsonify("Mock Server 101")


@api.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200


@api.route('/users/<id>', methods=['GET'])
def get_user(id):
    global users
    index = find(users, "id", int(id))
    if(index != -1):
        return jsonify(users[index]), 200
    else:
        return jsonify(f"{id} not found"), 404


@api.route('/users', methods=['POST'])
def add_users():
    global users
    users = json.loads(request.data)
    return jsonify(users)


@api.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    global users
    index = find(users, "id", int(id))
    if(index != -1):
        removedUser = users[index]
        users.pop(index)
        return jsonify(removedUser), 200
    else:
        return jsonify(f"{id} not found"), 404


if __name__ == '__main__':
    api.run(debug=True)
