"""Script to seed database."""

import os
import json
import csv
import crud
import model
import server

os.system('dropdb locations')
os.system('createdb locations')


model.connect_to_db(server.app)
model.db.create_all()

with open('DoctorWhoEpisodesInfo.csv') as csv_file:
    episode_data = csv.reader(csv_file, delimter=',')
  

with open('dr_who_locations.csv') as csv_file:
    location_data = csv.reader(csv_file, delimter=',') 

episodes_in_db = []             
for episode in episode_data:
    season, episode_number, doctor, title, imdb, ep_id = (episode['season'],
                                    episode['episode_number'],
                                    episode['doctor'],
                                    episode['title'],
                                    episode['imdb'],
                                    episode['ep_id'])

    db_episode = crud.create_episode(season,
                                      episode_number,
                                      doctor,
                                      title, 
                                      imdb,
                                      ep_id)
    episodes_in_db.append(db_episode)


locations_in_db = []             
for location in location_data:
    location_id, address, longitude, latitude, ep_id = (location['location_id'],
                                    location['address'],
                                    location['longitude'],
                                    location['latitude'],
                                    location['ep_id'])

    db_location = crud.create_location(location_id,
                                        address,
                                      longitude,
                                      latitude,
                                      ep_id)
    locations_in_db.append(db_location)