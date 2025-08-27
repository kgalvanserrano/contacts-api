# create a contacts API using flask
# each contact has an id, name, email, and maybe phone

# routes
# GET /contacts -> list all
# GET /contacts/<id> -> get one
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

contacts = []

@app.route('/')
def index():
    return "index"

@app.route('/contacts', methods=['GET'])
def list_contacts():
    return jsonify(contacts)

@app.route('/contacts/<int:id>', methods=['GET'])
def get_contact(id):
    contact = next((contact for contact in contacts if contact['id'] == id), None)
    if contact is None:
        abort(404, description="Contact not found")
    return jsonify(contact)

@app.route('/contacts', methods=['POST'])
def create_contact():
    data = request.get_json()
    contacts.append(data)
    return jsonify(data), 201

@app.route('/contacts/<int:id>', methods=['PUT'])
def update_contact(id):
    data = request.get_json()
    if not data or not data.get('name'):
        abort(400, description="Name is required")
    return jsonify(data)

@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    global contacts
    contacts = [contact for contact in contacts if contact['id'] != id]
    return jsonify({"message": "Contact deleted"}), 204

if __name__ == '__main__':
    app.run(debug=True)