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
    """Returns all episodes"""

    return Episode.query.all()

def get_episode_by_id(ep_id):
    """Returns episode by id."""

    return Episode.query.get(ep_id)

def create_location(address, longitude, latitude, ep_id):
    """Create and return a new episode"""

    location = Location(address=address,
                        longitude=longitude,
                        latitude=latitude 
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


if __name__ == '__main__':
    from server import app
    connect_to_db(app)