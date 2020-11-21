"""CRUD Operations"""

from model import db, Episode, Location, connect_to_db

def create_episode(season, episode_number, doctor, title, imdb, ep_id, companion, guest_star):
    """Create and return a new episode"""

    episode = Episode(season=season, 
                        episode_number=episode_number, 
                        doctor=doctor, 
                        title=title, 
                        imdb=imdb, 
                        ep_id=ep_id,
                        companion=companion, 
                        guest_star=guest_star)

    db.session.add(episode)
    db.session.commit()

    return episode

def get_episodes():
    """Returns all episodes."""

    return db.session.query(Episode).all()

def get_episode_by_id(ep_id):
    """Returns episode by episode_id."""

    return db.session.query(Episode).filter(Episode.ep_id == ep_id).first()

def create_location(address, longitude, latitude, ep_id):
    """Create and return a new location"""

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

    return db.session.query(Location).join(Episode).filter(Location.location_id == location_id).first()

def get_location_by_ep_id(ep_id):
    """Returns locations by ep_id."""

    return db.session.query(Location).filter_by(ep_id = ep_id).all()

def get_location_by_season_episode(season, episode_number):
    """Returns locations by season and episode."""

    return db.session.query(Location).join(Episode).filter(Episode.season == season, 
    Episode.episode_number == episode_number).all()

def get_location_by_doctor(doctor):
    """Returns locations by doctor."""

    return db.session.query(Location).join(Episode).filter(Episode.doctor == doctor).all()

def get_location_by_companion(companion):
    """Returns locations by companion."""

    return db.session.query(Location).join(Episode).filter(Episode.companion == companion).all()

def get_location_by_guest_star(guest_star):
    """Returns locations by guest star."""

    return db.session.query(Location).join(Episode).filter(Episode.guest_star == guest_star).all()

def get_location_by_title(title):
    """Returns locations by title."""

    return db.session.query(Location).join(Episode).filter(Episode.title.like('%title%')).all()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)