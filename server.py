"""Server for doctor who locations app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from model import connect_to_db, db, Episode, Location
import crud
from jinja2 import StrictUndefined
import os

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined
# GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/about')
def get_about_page():
    """View About page."""

    return render_template('about.html')


@app.route('/map_search/<season>/<episode_number>')
def create_map_from_season_search(season, episode_number):
    """Renders map template from search criteria by season and episode number."""
    
    if season == "SHOW ALL":
        all_locations = crud.get_locations()
        return render_template('map_search.html', locations=all_locations)
    else:
        locations_by_season_episode = crud.get_location_by_season_episode(season, episode_number)
        return render_template('map_search.html', locations=locations_by_season_episode)

@app.route('/map_search/<doctor>')
def create_map_from_doctor_search(doctor):
    """Renders map template from search criteria by doctor."""
    
    locations_by_doctor = crud.get_location_by_doctor(doctor)
    
    return render_template('map_search.html', locations=locations_by_doctor)


@app.route('/map_search/<title>')
def create_map_from_title_search(title):
    """Renders map template from search criteria by episode title.""" 

    locations_by_title = crud.get_location_by_title(title)

    return render_template('map_search.html', locations=locations_by_title)


@app.route("/single_map")
def show_single_map(location_id):
    """View map of single pin."""

    location_by_id = crud.get_location_by_id(location_id)
    
    return render_template('/single_map.html', location_by_id=location_by_id)

@app.route("/episode_list")
def create_list_of_episodes():
    """View full list of episodes."""

    list_of_episodes = crud.get_episodes()

    return render_template('episode_list.html', list_of_episodes=list_of_episodes)
                                
@app.route("/locations.json")
def location_info():
    """JSON information about filming locations."""

    film_locations = [
        {
            "location_id": location.location_id,
            "address": location.address,
            "longitude": location.longitude,
            "latitude": location.latitude,
            "ep_id": location.ep_id,
            "season": episode.season,
            # "episode_number": location.episode.episode_number,
            # "doctor": location.episode.doctor,
            # "title": location.episode.title,
            # "imdb": location.episode.imdb
        }
        for location in db.session.query(Location).join(Episode).all()
        # for location in Location.query.all()
    ]

    return jsonify(film_locations)

# @app.route("/locations_by_season.json")
# def filter_locations_by_season():
#     """Filtered location data in JSON format"""
#     seasoned_filtered_locations = [
#         {
#             "location_id": location.location_id,
#             "address": location.address,
#             "longitude": location.longitude,
#             "latitude": location.latitude,
#             "ep_id": location.ep_id,
#             "season": location.season,
#             "episode_number": location.episode_number,
#             "doctor": location.doctor,
#             "title": location.title,
#             "imdb": location.imdb
#         }
#      for location in db.session.query(Location).join(Episode)filter    .all()

#     return jsonify(season_filtered_locations)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
   