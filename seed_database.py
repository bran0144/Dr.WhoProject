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

# with open('DoctorWhoEpisodesInfo.csv') as csv.file:
    # csv_reader = csv.reader(csv_file, delimter=',')
#   episode_data =   

# with open('dr_who_locations.csv') as csv.file:
    # csv_reader = csv.reader(csv_file, delimter=',')
#   location_data =  

# episodes_in_db = []             - for loop to supply arguments to crud.create_episode
# for episode in episode_data:
#     season, episode_number, doctor, title, imdb, ep_id = (episode['season'],
#                                     episode['episode_number'],
#                                     episode['doctor'],
#                                     episode['doctor'],
#                                     episode['title'],
#                                     episode['imdb'],
#                                     episode['ep_id'])

#     db_episode = crud.create_episode(season,
#                                       episode_number,
#                                       doctor,
#                                       title, 
#                                       imdb,
#                                       ep_id)
#     episodes_in_db.append(db_episodes)


# locations_in_db = []             - for loop to supply arguments to crud.create_location
# for location in location_data:
#     address, longitude, latitude, ep_id = (location['address'],
#                                     location['longitude'],
#                                     location['latitude'])
#                                     location['ep_id'])

#     db_location = crud.create_location(address,
#                                       longitude,
#                                       latitude,
#                                       ep_id)
#     locations_in_db.append(db_locations)