"""Data Models for Dr. WHO app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Episode(db.Model):
    """An episode"""

    __tablename__ = 'episodes'

    ep_id = db.Column(db.String(10), primary_key=True)
    season = db.Column(db.String(15), nullable=False)
    episode_number = db.Column(db.String(10), nullable=False)
    doctor = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    imdb = db.Column(db.Text, nullable=False)
    companion = db.Column(db.String(50), nullable=False)
    guest_star = db.Column(db.String(50))


    def __repr__(self):
        return f'<episode_id={self.ep_id} title={self.title}>'


class Location(db.Model):
    """A location"""

    __tablename__ = 'locations'

    location_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    address = db.Column(db.String, nullable=False)
    longitude = db.Column(db.Numeric(precision=20, scale=15), nullable=False)
    latitude = db.Column(db.Numeric(precision=20, scale=15), nullable=False)
    ep_id = db.Column(db.String(10), db.ForeignKey('episodes.ep_id'))

    episodes = db.relationship('Episode', backref='locations')

    def __repr__(self):
        return f'<Location location_id={self.location_id} longitude={self.longitude} latitude={self.latitude} ep_id={self.ep_id}>'


def example_data():
    """Fake data for testing in tests.py"""
    Episode.query.delete()
    Location.query.delete()

    #Sample episode and location data for testing database
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


def connect_to_db(flask_app, db_uri='postgresql:///locations', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    #flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
