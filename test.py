import unittest
import json
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_hello_from_root(self):
        response = self.app.get('/')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Automate all the things!')
        self.assertIsNotNone(data['timestamp'])

    def test_resource_not_found(self):
        response = self.app.get('/wrong-url')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['error'], 'Not found!')

if __name__ == '__main__':
    unittest.main()