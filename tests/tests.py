import unittest
from server import app
from model import Episode, Location
from selenium import webdriver

class TestWebApp(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:5000/')
        self.assertEqual(self.browser.title, '')

class FlaskTests(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

        connect_to_db(app, 'postgresql:///testdb')
        db.create_all()
        example_data()

    def test_homepage(self):

        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn('<h1>Test</h1>', result.data)


def example_data():
    Episode.query.delete()
    Location.query.delete()

    ep1 = Episode(ep_id='17_2', season=17, episode_number=2, doctor='Hiddleston', title='Doctor Loki',
     imdb='http://www.imdb.com', companion='Irene Adler', guest_star='Captain Jack Harkness')

    ep2 = Episode(ep_id='17_3', season=17, episode_number=3, doctor='Hiddleston', title='Marvel', 
    imdb='http://www.imdb.com', companion='Irene Adler', guest_star='Rose Tyler')

    ep3 = Episode(ep_id='17_4', season=17, episode_number=4, doctor='Hiddleston', title='Gallifrey falls again',
    imdb='http://www.imdb.com', compansion='Irene Adler', guest_star='Martha Jones')

    loc1 = Location(address='26 Spencer St, Cardiff CF24 4PG, UK', longitude=-3.17671015211488, latitude=51.4972798678649,
    ep_id='17_2')

    loc2 = Location(address='4 Bryn-y-Mor, West Aberthaw, Barry CF62 4HZ, UK', longitude=-3.40045689814759, latitude=51.3950533721374,
    ep_id='17_3')

    loc3 = Location(address="St Donat's Castle, Llantwit Major CF61 1WF, UK", longitude=-3.53334903717,latitude=51.4018629428,
    ep_id='17_4')

    db.session.add_all([ep1, ep2, ep3, loc1, loc2, loc3])
    db.session.commit()



