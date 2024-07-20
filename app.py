#phase2
 
#Flask Application with SQLAlchemy

from flask import Flask, jsonify, request

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Employee(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(50), nullable=False)

    age = db.Column(db.Integer, nullable=False)

    department = db.Column(db.String(50), nullable=False)

    def _repr_(self):

        return f'<Employee {self.name}>'

db.create_all()

@app.route('/employees', methods=['POST'])

def create_employee():

    data = request.get_json()

    new_employee = Employee(name=data['name'], age=data['age'], department=data['department'])

    db.session.add(new_employee)

    db.session.commit()

    return jsonify({"id": new_employee.id, "name": new_employee.name, "age": new_employee.age, "department": new_employee.department}), 201

@app.route('/employees', methods=['GET'])

def get_employees():

    employees = Employee.query.all()

    return jsonify([{"id": emp.id, "name": emp.name, "age": emp.age, "department": emp.department} for emp in employees])

@app.route('/employees/<int:id>', methods=['GET'])

def get_employee(id):

    employee = Employee.query.get_or_404(id)

    return jsonify({"id": employee.id, "name": employee.name, "age": employee.age, "department": employee.department})

@app.route('/employees/<int:id>', methods=['PUT'])

def update_employee(id):

    data = request.get_json()

    employee = Employee.query.get_or_404(id)

    employee.name = data['name']

    employee.age = data['age']

    employee.department = data['department']

    db.session.commit()

    return jsonify({"id": employee.id, "name": employee.name, "age": employee.age, "department": employee.department})

@app.route('/employees/<int:id>', methods=['DELETE'])

def delete_employee(id):

    employee = Employee.query.get_or_404(id)

    db.session.delete(employee)

    db.session.commit()

    return '', 204

if __name__ == '_main_':

    app.run(debug=True)