import server
import unittest

class AppIntegrationTestCase(unittest.TestCase):

    def setUp(self):
        self.client = server.app.test_client()
        server.app.config['TESTING'] = True

    def tearDown(self):
        return

    def test_index(self):
        client = server.app.test_client()
        result = client.get('/')
        self.assertIn(b'<option value="1">1</option>', result.data)
    
    def test_episode_list(self):
        client = server.app.test_client()
        result = client.get('/episode_list')
        self.assertIn(b'"The End of the World" Doctor: Eccleston Companion: Rose Tyler', result.data)

    def test_additional_info(self):
        client = server.app.test_client()
        result = client.get('/additional_info')
        self.assertIn(b'<p><a href="https://www.youtube.com/watch?v=E33vAhs4bNs">Link to Video</a></p>', result.data)

    def test_about(self):
        client = server.app.test_client()
        result = client.get('/about')
        self.assertIn(b'<h2>About Me</h2>', result.data)

    def test_map_search_season(self):
        client = server.app.test_client()
        result = client.get('/map_search_season')
        self.assertIn(b'', result.data)

    def test_map_search_doctor(self):
        client = server.app.test_client()
        result = client.get('/map_search_doctor')
        self.assertIn(b'', result.data)

    def test_map_search_companion(self):
        client = server.app.test_client()
        result = client.get('/map_search_companion')
        self.assertIn(b'', result.data)

    def test_map_search_guest_star(self):
        client = server.app.test_client()
        result = client.get('/map_search_guest_star')
        self.assertIn(b'', result.data)
    
    def test_map_search_title(self):
        client = server.app.test_client()
        result = client.get('/map_search_title')
        self.assertIn(b'', result.data)
    
    def test_single_map(self):
        client = server.app.test_client()
        result = client.get('/single_map')
        self.assertIn(b'', result.data)


if __name__ == '__main__':
    unittest.main()