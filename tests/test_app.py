import unittest
import json
from app import app
from database import ScrapeJob, ScrapeResult

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_start_endpoint(self):
        response = self.app.post('/start', json={'url': 'http://example.com'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('job_id', data)
        self.assertIsInstance(data['job_id'], int)

    def test_results_endpoint(self):
        # Assuming job_id 1 exists and has completed
        response = self.app.get('/results?job_id=1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(data, list)
        self.assertTrue(all(isinstance(item, ScrapeResult) for item in data))

    def test_status_endpoint(self):
        # Assuming job_id 1 exists
        response = self.app.get('/status?job_id=1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('status', data)
        self.assertIn(data['status'], ['pending', 'in progress', 'completed', 'failed'])

    def test_start_endpoint_authentication(self):
        # Assuming authenticate decorator returns 401 for unauthorized access
        response = self.app.post('/start', json={'url': 'http://example.com'}, headers={'Authorization': 'InvalidToken'})
        self.assertEqual(response.status_code, 401)

    def test_results_endpoint_no_job_id(self):
        response = self.app.get('/results')
        self.assertEqual(response.status_code, 400)

    def test_status_endpoint_no_job_id(self):
        response = self.app.get('/status')
        self.assertEqual(response.status_code, 400)

    def test_start_endpoint_bad_request(self):
        response = self.app.post('/start', json={})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()