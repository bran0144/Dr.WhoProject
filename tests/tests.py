import unittest
from server import app
from model import connect_to_db, db, example_data
from flask import session

class FlaskTestsDataBase(unittest.TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

        connect_to_db(app, 'postgresql:///testdb')
        db.create_all()
        example_data()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        db.engine.dispose()

    def test_episode_list(self):
        result = self.client.get("/episodes_list")
        self.assertIn(b"Doctor Loki", result.data)
    
    def test_map_search_doctor(self):
        result = self.client.get("/map_search_doctor", data={"doctor": "Hiddleston"})
        self.assertIn(b"Hiddleston", result.data)

    def test_map_search_companion(self):
        result = self.client.get("/map_search_companion", data={"companion":"Irene Adler"})
        self.assertIn(b"Irene Adler", result.data)

    def test_map_search_title(self):
        result = self.client.get("/map_search_title", data={"title": "Marvel"})
        self.assertIn(b"Marvel", result.data)

    def test_map_search_guest_star(self):
        result = self.client.get("/map_search_guest_star", data={"guest_star": "Captain Jack Harkness"})
        self.assertIn(b"Captain Jack Harkness", result.data)

    def test_map_search_season(self):
        result = self.client.get("/map_search_season", data={"season": 17, "episode": 2})
        self.assertIn(b"17", result.data)
    
if __name__ == "__main__":
    import unittest
    unittest.main()
