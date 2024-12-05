import unittest
import json
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_hello_endpoint(self):
        response = self.client.get("/api/test")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello World!"})

    def test_add_endpoint(self):
        payload = json.dumps({"number_1": 5, "number_2": 3})
        response = self.client.post(
            "/api/add", data=payload, content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"result": 8})

    def test_add_invalid_input(self):
        payload = json.dumps({"number_1": 5})
        response = self.client.post(
            "/api/add", data=payload, content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"error": "Invalid input"})