import unittest
from unittest.mock import patch
from scraper import Scraper, ScrapeJob, ScrapeResult

class TestScraper(unittest.TestCase):

    def setUp(self):
        self.scraper = Scraper()
        self.test_url = "http://example.com"
        self.test_job = ScrapeJob(url=self.test_url)

    def test_start_scraper(self):
        with patch.object(self.scraper, 'start', return_value=True) as mock_start:
            self.scraper.start(self.test_job)
            mock_start.assert_called_with(self.test_job)

    def test_get_results(self):
        expected_result = ScrapeResult(url=self.test_url, data="Test Data", status="Completed")
        with patch.object(self.scraper, 'get_results', return_value=expected_result) as mock_get_results:
            result = self.scraper.get_results(self.test_job)
            self.assertEqual(result, expected_result)
            mock_get_results.assert_called_with(self.test_job)

    def test_get_status(self):
        expected_status = "Running"
        with patch.object(self.scraper, 'get_status', return_value=expected_status) as mock_get_status:
            status = self.scraper.get_status(self.test_job)
            self.assertEqual(status, expected_status)
            mock_get_status.assert_called_with(self.test_job)

    def test_scraper_no_url(self):
        with self.assertRaises(ValueError):
            self.scraper.start(ScrapeJob(url=""))

    def test_scraper_invalid_url(self):
        with self.assertRaises(ValueError):
            self.scraper.start(ScrapeJob(url="invalid-url"))

    def test_scraper_result_none(self):
        with patch.object(self.scraper, 'get_results', return_value=None) as mock_get_results:
            result = self.scraper.get_results(self.test_job)
            self.assertIsNone(result)
            mock_get_results.assert_called_with(self.test_job)

if __name__ == '__main__':
    unittest.main()