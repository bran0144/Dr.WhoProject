"""Server for doctor who locations app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from model import connect_to_db, db, Episode, Location
import crud
from jinja2 import StrictUndefined
import os
import json

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


@app.route('/map_search_season')
def create_map_from_season_search():
    """Renders map template from search criteria by season and episode number."""
    
    season = request.args.get("season")
    episode = request.args.get("episode")

    if season == "SHOW ALL":
        all_locations = crud.get_locations()
        return render_template('map_search.html', locations=all_locations)
    else:
        locations_by_season_episode = crud.get_location_by_season_episode(season, episode)
        return render_template('map_search.html', locations=locations_by_season_episode)

@app.route('/map_search_doctor')
def create_map_from_doctor_search():
    """Renders map template from search criteria by doctor."""
    
    doctor = request.args.get("doctor")
    
    locations_by_doctor = crud.get_location_by_doctor(doctor)
    
    json_locations = json.dumps(locations_by_doctor)
    return render_template('map_search.html', locations=json_locations)


@app.route('/map_search_title')
def create_map_from_title_search():
    """Renders map template from search criteria by episode title.""" 

    title = request.args.get("title")

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
                                
@app.route("/episodes.json")
def location_info():
    """JSON information about filming locations."""

    episode_info = [
        {
            "season": episode.season,
            "episode_number": episode.episode_number,
            "doctor": episode.doctor,
            "title": episode.title,
            "imdb": episode.imdb,
            "ep_id": episode.ep_id
        }
        for episode in db.session.query(Episode).join(Location).all()
    ]

    return jsonify(episode_info)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
   