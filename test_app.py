#phase3

import unittest

from app import app, db, Employee

class EmployeeTestCase(unittest.TestCase):

    def setUp(self):

        app.config['TESTING'] = True

        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

        self.app = app.test_client()

        db.create_all()

    def tearDown(self):

        db.session.remove()

        db.drop_all()

    def test_create_employee(self):

        response = self.app.post('/employees', json={

            "name": "John Doe",

            "age": 30,

            "department": "Engineering"
        })

        self.assertEqual(response.status_code, 201)

        self.assertIn("John Doe", str(response.data))

    def test_get_all_employees(self):

        self.app.post('/employees', json={

            "name": "John Doe",

            "age": 30,

            "department": "Engineering"

        })

        response = self.app.get('/employees')

        self.assertEqual(response.status_code, 200)

        self.assertIn("John Doe", str(response.data))

    def test_get_employee(self):

        self.app.post('/employees', json={

            "name": "John Doe",

            "age": 30,

            "department": "Engineering"

        })

        response = self.app.get('/employees/1')

        self.assertEqual(response.status_code, 200)

        self.assertIn("John Doe", str(response.data))

    def test_update_employee(self):

        self.app.post('/employees', json={

            "name": "John Doe",

            "age": 30,

            "department": "Engineering"

        })

        response = self.app.put('/employees/1', json={

            "name": "Jane Doe",

            "age": 32,

            "department": "HR"

        })

        self.assertEqual(response.status_code, 200)

        self.assertIn("Jane Doe", str(response.data))

    def test_delete_employee(self):

        self.app.post('/employees', json={

            "name": "John Doe",

            "age": 30,

            "department": "Engineering"

        })

        response = self.app.delete('/employees/1')

        self.assertEqual(response.status_code, 204)

if __name__ == '_main_':
   
   unittest.main()