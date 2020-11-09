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

    return db.session.query(Episode).all()

def create_location(address, longitude, latitude, ep_id):
    """Create and return a new episode"""

    location = Location(address=address,
                        longitude=longitude,
                        latitude=latitude, 
                        ep_id=ep_id)

    db.session.add(location)
    db.session.commit()

    return location

def get_locations():
    """Returns all locations."""

    return db.session.query(Location).all()

def get_location_by_id(location_id):
    """Returns location by id."""

    return db.session.query(Location).filter(Location.location_id == location_id).all()

def get_location_by_ep_id(ep_id):
    """Returns locations by ep_id."""

    return db.session.query(Location).filter(Location.ep_id == ep_id).all()

def get_location_by_season_episode(season, episode_number):
    """Returns locations by season and episode."""

    return db.session.query(Location).join(Episode).filter(Episode.season == season, 
    Episode.episode_number == episode_number).all()

def get_location_by_doctor(doctor):
    """Returns locations by doctor."""

    return db.session.query(Location).join(Episode).filter(Episode.doctor == doctor).all()

def get_location_by_title(title):
    """Returns locations by title."""

    return db.session.query(Location).join(Episode).filter(Episode.title.like('%title%')).all()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)