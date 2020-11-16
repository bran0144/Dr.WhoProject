from unittest import TestCase
from server import app

class FlaskTests(TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def tearDown(self):

    def test_map_search(self):
        result = self.client.get('/map_search_season')
        self.assertEqual(result.status_code, 200)
        self.assertIn('', result.data)


if __name__ == '__main__':
    unittest.main()