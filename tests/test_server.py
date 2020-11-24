import server
import unittest

class AppIntegrationTestCase(unittest.TestCase):

    def setUp(self):
        self.client = server.app.test_client()
        server.app.config['TESTING'] = True

    def tearDown(self):
        return

    def test_index(self):
        """Tests homepage."""
        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'<option value="1">1</option>', result.data)
    
    def test_episode_list(self):
        """Tests episode list page."""
        result = self.client.get('/episode_list')
        self.assertIn(b'"The End of the World" Doctor: Eccleston Companion: Rose Tyler', result.data)

    def test_additional_info(self):
        """Tests additional info page."""
        result = self.client.get('/additional_info')
        self.assertIn(b'<p><a href="https://www.youtube.com/watch?v=E33vAhs4bNs">Link to Video</a></p>', result.data)

    def test_about(self):
        """Tests about page."""
        result = self.client.get('/about')
        self.assertIn(b'<h2>About Me</h2>', result.data)

    def test_single_map(self):
        """Tests single map page."""
        result = self.client.get('/single_map')
        self.assertIn(b'<div id="single_map"></div>', result.data)


if __name__ == '__main__':
    unittest.main()