![alt text](https://github.com/bran0144/Dr.WhoProject/blob/master/static/img/logo.png "Logo Title Text 1")

## Introduction:

As a fan of both travel and Doctor Who, I wanted to create a searchable database that allowed the user to search for their favorite film sites from the popular show and create maps of those sites.

### Features:

- Allow user to search by season and episode, by title, by Doctor, by companion, or by guest star
- Displays multiple sites on a map that includes an information box that pops up on mouseover with information about the episode 
- Infowindow uses an AJAX call to get data from API I created of the relevant episode info
- Allows user to click from pin on map page to page with a single site and additional information including a link to IMDB page about episode
- Includes a full episode list with links to relevant map and IMDB page
- Includes an additional page with the most iconic sites from Doctor Who, links to youtube videos showing the relevant scenes from Doctor Who at the site, and links to information about visiting that site
- Designed logo for website in Paint S for Mac

### Video Demo:
[Link to YouTube Demo](https://youtu.be/k80PL-FMAiM)

### Landing Page
![alt text](https://github.com/bran0144/Dr.WhoProject/blob/master/static/img/landingpage.png "Landing Page")

### Map Page
![alt text](https://github.com/bran0144/Dr.WhoProject/blob/master/static/img/searched_map.png "Map Page")

### InfoWindow
![alt text](https://github.com/bran0144/Dr.WhoProject/blob/master/static/img/info_window.png "Info Window")

### Single Pin Page
![alt text](https://github.com/bran0144/Dr.WhoProject/blob/master/static/img/singlePin.png "Single Pin Page")

### Additional Sites
![alt text](https://github.com/bran0144/Dr.WhoProject/blob/master/static/img/additional_sites.png "Additional Sites")

### Episode List
![alt text](https://github.com/bran0144/Dr.WhoProject/blob/master/static/img/episode_list.png "Episode List")

#### Languages:

- Python
- Javascript/jQuery
- AJAX 
- CSS
- HTML
- PostgresSQL
- Jinja

#### Framework/libraries:
- Flask
- Bootstrap

#### APIs: 
- Google Maps Javascript API
- Created an API of episode info for Google Maps to call using AJAX 

#### Future State

- I hope to extend the project to include a user login to allow the user to save their favorite sites and create printable maps
- I would like to expand the database to include a many-to-many relationship for the few sites that appear in multiple episodes and for the few episodes that include multiple Doctors

#### Running Locally:

In terminal, run "python3 server.py" from root directory

#### Author:

**Katie Gott**- *Software developer currently seeking new opportunities* - [Linkedin][https://www.linkedin.com/in/katie-gott/] 

#### Thanks:
Special thanks to moviemaps.org who shared their Doctor Who film locations data with me for my project.