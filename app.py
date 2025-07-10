from flask import Flask, jsonify

app = Flask(__name__)

<<<<<<< HEAD
#  Dummy Users Table (10 fake entries)
=======
# Dummy Users Table (10 fake entries)
>>>>>>> c13021773ef51c7620f31e68777724a1cc440476
users = [
    {"id": 1, "name": "Amit", "email": "amit@example.com"},
    {"id": 2, "name": "Sita", "email": "sita@example.com"},
    {"id": 3, "name": "Rahul", "email": "rahul@example.com"},
    {"id": 4, "name": "Anjali", "email": "anjali@example.com"},
    {"id": 5, "name": "Ravi", "email": "ravi@example.com"},
    {"id": 6, "name": "Neha", "email": "neha@example.com"},
    {"id": 7, "name": "Manoj", "email": "manoj@example.com"},
    {"id": 8, "name": "Pooja", "email": "pooja@example.com"},
    {"id": 9, "name": "Vikram", "email": "vikram@example.com"},
    {"id": 10, "name": "Kiran", "email": "kiran@example.com"}
]

<<<<<<< HEAD
#  Home Route
@app.route('/')
def home():
    return "Flask User API is Running"
=======
# Home Route
@app.route('/')
def home():
    return " Flask User API is Running"
>>>>>>> c13021773ef51c7620f31e68777724a1cc440476

# GET /user API
@app.route('/user', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)

