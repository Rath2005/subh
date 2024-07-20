#phase1
 
#Basic Flask Application

from flask import Flask, jsonify, request

app = Flask(__name__)

# Basic routes

@app.route('/')

def home():

    return "Welcome to the Employee Management System"

@app.route('/hello', methods=['GET'])

def hello():

    return jsonify({"message": "Hello, World!"})

# Sample in-memory storage for Phase 1

employees = []

@app.route('/employee', methods=['POST'])

def create_employee():

    data = request.get_json()

    employees.append(data)

    return jsonify(data), 201

@app.route('/employees', methods=['GET'])

def get_employees():

    return jsonify(employees)

@app.route('/employee/<int:id>', methods=['PUT'])

def update_employee(id):

    data = request.get_json()

    for employee in employees:

        if employee['id'] == id:

            employee.update(data)

            return jsonify(employee)
        
    return jsonify({"error": "Employee not found"}), 404

@app.route('/employee/<int:id>', methods=['DELETE'])

def delete_employee(id):

    global employees

    employees = [employee for employee in employees if employee['id'] != id]

    return '', 204

if __name__ == '_main_':
    
    app.run(debug=True)