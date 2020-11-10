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
        return f'<Location location_id={self.location_id} longitude={self.longitude} latitude={self.latitude}>'


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
