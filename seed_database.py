"""Script to seed database."""

import os
import json
import pandas as pd


import crud
import model
import server

os.system('dropdb locations')
os.system('createdb locations')


model.connect_to_db(server.app)
model.db.create_all()

# with open('') as f:
#     location_data =   - look up how to do this with xlsx files and I need to do two files

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