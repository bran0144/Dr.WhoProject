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

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/about')
def get_about_page():
    """View About page."""

    return render_template('about.html')

@app.route('/additional_info')
def get_additionalinfo_page():
    """View Additional Info page."""

    return render_template('additional_info.html')


@app.route('/map_search_season')
def create_map_from_season_search():
    """Renders map template from search criteria by season and episode number."""
    
    season = request.args.get("season")
    episode = request.args.get("episode")

    locations_by_season = [
        {
            "latitude": str(location.latitude),
            "longitude": str(location.longitude),
            "ep_id": location.ep_id,
            "address": location.address,
            "location_id": location.location_id

        }
        for location in crud.get_location_by_season_episode(season, episode)
    ]
       
    return render_template('map_search.html', locations=locations_by_season)

@app.route('/map_search_doctor')
def create_map_from_doctor_search():
    """Renders map template from search criteria by doctor."""
    
    doctor = request.args.get("doctor")
    
    locations_by_doctor = [
        {
            "latitude": str(location.latitude),
            "longitude": str(location.longitude),
            "ep_id": location.ep_id,
            "address": location.address,
            "location_id": location.location_id

        }
        for location in crud.get_location_by_doctor(doctor)
    ]

    return render_template('map_search.html', locations=locations_by_doctor)

@app.route('/map_search_companion')
def create_map_from_companion_search():
    """Renders map template from search criteria by companion."""
    
    companion = request.args.get("companion")
    
    locations_by_companion = [
        {
            "latitude": str(location.latitude),
            "longitude": str(location.longitude),
            "ep_id": location.ep_id,
            "address": location.address,
            "location_id": location.location_id

        }
        for location in crud.get_location_by_companion(companion)
    ]

    return render_template('map_search.html', locations=locations_by_companion)   

@app.route('/map_search_guest_star')
def create_map_from_guest_star_search():
    """Renders map template from search criteria by guest star."""
    
    guest_star = request.args.get("guest_star")
    
    locations_by_guest_star = [
        {
            "latitude": str(location.latitude),
            "longitude": str(location.longitude),
            "ep_id": location.ep_id,
            "address": location.address,
            "location_id": location.location_id

        }
        for location in crud.get_location_by_guest_star(guest_star)
    ]

    return render_template('map_search.html', locations=locations_by_guest_star)
       
@app.route('/map_search_title')
def create_map_from_title_search():
    """Renders map template from search criteria by episode title.""" 

    title = request.args.get("title")

    locations_by_title = [
        {
            "latitude": str(location.latitude),
            "longitude": str(location.longitude),
            "ep_id": location.ep_id,
            "address": location.address,
            "location_id": location.location_id
        }
        for location in crud.get_location_by_title(title)
    ]

    return render_template('map_search.html', locations=locations_by_title)


@app.route("/single_map/<location_id>")
def show_single_map(location_id):
    """View map of single pin."""
    
    location = crud.get_location_by_id(location_id)

    location_by_id = {"latitude": str(location.latitude),
            "longitude": str(location.longitude),
            "ep_id": location.ep_id,
            "address": location.address,
            "season":location.episodes.season,
            "episode_number": location.episodes.episode_number,
            "title": location.episodes.title,
            "doctor": location.episodes.doctor,
            "companion": location.episodes.companion,
            "guest_star": location.episodes.guest_star,
            "imdb": location.episodes.imdb
            }
           
    return render_template('/single_map.html', location_by_id=location_by_id)

@app.route("/episode_list")
def create_list_of_episodes():
    """View full list of episodes."""

    list_of_episodes = crud.get_episodes()

    return render_template('episode_list.html', episodes=list_of_episodes)
                                
@app.route("/api/episodes/<ep_id>")
def episode_info(ep_id):
    """JSON information about episodes."""

    episode = crud.get_episode_by_id(ep_id)
    episode_info = {
            "season": episode.season,
            "episode_number": episode.episode_number,
            "doctor": episode.doctor,
            "title": episode.title,
            "companion": episode.companion,
            "guest_star": episode.guest_star,
            "imdb": episode.imdb,
            "ep_id": episode.ep_id
        }

    return jsonify(episode_info)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
   