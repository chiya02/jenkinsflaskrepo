import unittest
from app import app


class BasicTests(unittest.TestCase):

    def test_app_test_client(self):
        tester = app.test_client(self)
        response = tester.get("/", content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello, Jenkins CI/CD from Flask App Windows!")


if __name__ == "__main__":
    unittest.main()
