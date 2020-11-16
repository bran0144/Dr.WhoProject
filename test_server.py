import unittest

class MyAppIntegrationTestCase(unittest: TestCase):

    def text_index(self):
        client = server.app.test_client()
        result = client.get('/')
        self.assertIn(b'<select name="season" id="season">', result.data)

    def test_map_search(self):
        client = server.app.test_client()
        result = client.post('/map_search_season', query_string={'season': '1'})
        self.assertIn(b'')