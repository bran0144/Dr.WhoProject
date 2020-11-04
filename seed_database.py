"""Script to seed database."""

import os
import csv
import crud
import model
import server

os.system('dropdb locations')
os.system('createdb locations')

model.connect_to_db(server.app)
model.db.create_all()

locations_in_db = [] 


# with open('data/DoctorWhoEpisodesInfo.csv') as csv_file:
#     fieldnames = ['season', 'episode_number', 'doctor', 'title', 'imdb', 'ep_id']
#     episode_data = csv.DictReader(csv_file, fieldnames=fieldnames, dialect='excel')
#     #reads and imports Episode info from csv file    

#     for episode in episode_data:
       
#     #for loop to set up database for episodes table and seeds data into episodes_in_db

#         season, episode_number, doctor, title, imdb, ep_id = (episode['season'],
#                                         episode['episode_number'],
#                                         episode['doctor'],
#                                         episode['title'],
#                                         episode['imdb'],
#                                         episode['ep_id'])
        

#         db_episode = crud.create_episode(season,
#                                         episode_number,
#                                         doctor,
#                                         title, 
#                                         imdb,
#                                         ep_id)
#         locations_in_db.append(db_episode)


with open('data/dr_who_locations.csv') as csv_file:
    fieldnames = ['address', 'longitude', 'latitude', 'ep_id']
    location_data = csv.DictReader(csv_file, fieldnames=fieldnames, dialect='excel') 
    #reads and imports Location info from csv file

    for location in location_data:
     #for loop to set up database for locations table and seeds data into locations_in_db
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