"""Models for Dr. WHO app"""

from flask_sqlalchmey import SQLAlchemy

db = SQLAlchemy()

class Episode(db.Model):
    """An episode"""

    __tablename__ = 'episodes'

    ep_id = db.Column(db.String(10), primary_key=True)
    season = db.Column(db.Intger, nullable=False)
    episode = db.Column(db.Intger, nullable=False)
    doctor = db.Column(db.String(30), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    imdb = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<episode_id={ep_id} title={title}>'


class Location(db.Model):
    """A location"""

    __tablename__ = 'locations'

    location_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    ep_id = db.Column(db.String, db.ForeignKey(episodes.ep_id))

    episodes = db.relationship( 'Episode', backref='locations')

    def __repr__(self):
        return f'<Location location_id={location_id} name={name}>'


def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    #flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app


    connect_to_db(app)
