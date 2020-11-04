"""CRUD Operations"""

from model import db, Episode, Location, connect_to_db

def create_episode(season, episode_number, doctor, title, imdb, ep_id):
    """Create and return a new episode"""

    episode = Episode(season=season, 
                        episode_number=episode_number, 
                        doctor=doctor, 
                        title=title, 
                        imdb=imdb, 
                        ep_id=ep_id)

    db.session.add(episode)
    db.session.commit()

    return episode

def get_episodes():
    """Returns all locations."""

    return Episode.query.all()

def create_location(location_id, address, longitude, latitude, ep_id):
    """Create and return a new episode"""

    location = Location(location_id=location_id,
                        address=address,
                        longitude=longitude,
                        latitude=latitude, 
                        ep_id=ep_id)

    db.session.add(location)
    db.session.commit()

    return location

def get_locations():
    """Returns all locations."""

    return Location.query.all()

def get_location_by_id(location_id):
    """Returns location by id."""

    return Location.query.get(location_id)

def get_location_by_ep_id(ep_id):
    """Returns locations by ep_id."""

    return Location.query.get(ep_id)

def get_location_by_season_episode(season, episode_number):
    """Returns locations by season and episode."""

    return Location.query.options(db.joinedload('episodes')).filter_by(season=season, 
    episode_number=episode_number, title=title).get(longitude=longitude, latitude=latitude)

def get_location_by_doctor(doctor):
    """Returns locations by doctor."""

    return Location.query.options(db.joinedload('episodes')).get(doctor)

def get_location_by_title(title):
    """Returns locations by title."""

    return Location.query.options

if __name__ == '__main__':
    from server import app
    connect_to_db(app)