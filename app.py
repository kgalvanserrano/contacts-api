# create a contacts API using flask
# each contact has an id, name, email, and maybe phone

# routes
# GET /contacts -> list all
# POST /contacts -> create one
# PUT /contacts/<id> -> update one
# DELETE /contacts/<id> -> delete one

# data storage
# start with in-memory list/dict
# then level up to a simple SQLite or json

# testing
# use curl or Postman to test endpoints
# example -> curl -X POST http://localhost:5000/contacts -H "Content-Type: application/json" -d '{"name":"Kevin","email":"kevin@example.com"}'

# stretch goals
# add input validation (e.g reject empty names)
# return proper HTTP status codes (201 on create, 404 on not found)
# try adding pagination (GET /contacts?page=1&limit=10)
# add search (GET /contacts?name=Kevin)

from flask import Flask, request, jsonify, abort

app = Flask(__name__)

@app.route('/')
def index():
    return "index"

@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    pass

if __name__ == '__main__':
    pass