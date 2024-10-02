import unittest
from backend.app import app


class FlaskTestCase(unittest.TestCase):

    def test_upload_no_file(self):
        tester = app.test_client(self)
        response = tester.post('/upload', content_type='multipart/form-data')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'No file part', response.data)

    def test_upload_empty_file(self):
        tester = app.test_client(self)
        data = {'file': (None, '')}
        response = tester.post('/upload', content_type='multipart/form-data', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'No selected file', response.data)


if __name__ == '__main__':
    unittest.main()
