import unittest
import json
from app import app

class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_status_200(self):
        response = self.app.get('http://127.0.0.1:5002/employees')
        self.assertEqual(response.status_code, 200)

    def test_status_404(self):
        response = self.app.get('http://127.0.0.1:5002/')
        self.assertEqual(response.status_code, 404)

    def test_json(self):
        response = self.app.get('http://127.0.0.1:5002/employees')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data, {u'employees': [1, 2, 3, 4, 5, 6, 7, 8]})

    def test_employees(self):
        response = self.app.get('http://127.0.0.1:5002/employees')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['employees'], [1, 2, 3, 4, 5, 6, 7, 8])
        

if __name__ == "__main__":
        unittest.main()
