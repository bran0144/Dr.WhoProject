"""Server for doctor who locations app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from model import connect_to_db, db, Episode, Location
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/map_search')
def create_map_from_season_search():
    """Renders map template from search criteria."""

    season = request.args.get('season')
    episode_number = request.args.get('episode_number')
    
    if season == "SHOW ALL":
        latitude, longitude, season, episode_number, title = crud.get_locations()
    else:
        latitude, longitude, season, episode_number, title = crud.get_location_by_season_episode(season, episode_number)
    
    return render_template('map_search.html',
                            latitude=latitude,
                            longtiude=longitude,
                            season=season,
                            episode_number=episode_number,
                            title=title)

@app.route('/map_search')
def create_map_from_doctor_search():
    """Renders map template from search criteria."""

    doctor = request.args.get('doctor')

    latitude, longitude, season, episode_number, title = crud.get_location_by_doctor(doctor)
    
    return render_template('map_search.html',
                            latitude=latitude,
                            longitude=longitude,
                            season=season,
                            episode_number=episode_number,
                            title=title,
                            doctor=doctor)

@app.route('/map_search')
def create_map_from_title_search():
    """Renders map template from search criteria.""" 

    title = request.args.get('title')

    latitude, longitude, season, episode_number, title = crud.get_location_by_title(title)

    return render_template('map_search.html',
                            latitude=latitude,
                            longitude=longitude,
                            season=season,
                            episode_number=episode_number,
                            title=title)


@app.route("/single_map")
def show_single_map(location_id):
    """View map of single pin."""

    # renders google map and info box
    # based on click of pin from searched map page

    latitude, longitude, address, season, episode_number, title, imdb = crud.get_location_by_id(location_id)
    
    return render_template('/single_map.html', latitude=latitude,
                                        longitude=longitude,
                                        address=address,
                                        season=season,
                                        episode_number=episode_number,
                                        title=title,
                                        imdb=imdb)

@app.route("/episode_list")
def create_list_of_episodes():
    """View full list of episodes."""

    season, episode_number, doctor, title, imdb = crud.get_episodes()

    return render_template('episode_list.html', season=season,
                                                episode_number=episode_number,
                                                doctor=doctor,
                                                title=title,
                                                imdb=imdb)
                                
@app.route("/api/locations")
def location_info():
    """JSON information about filming locations."""

    film_locations = [
        {
            "location_id": Location.location_id,
            "address": Location.address,
            "longitude": Location.longitude,
            "latitude": Location.latitude,
            "ep_id": Location.ep_id,
            "season": Episode.season,
            "episode_number": Episode.episode_number,
            "doctor": Episode.doctor,
            "title": Episode.title,
            "imdb": Episode.imdb
        }
        for location in Location.query.all()
    ]

    return jsonify(film_locations)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)