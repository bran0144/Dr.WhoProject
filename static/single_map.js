"use strict";


// Build a separate/permanent info box on single pin map (2nd sprint)

const address = location.address;
const latLng = {'lat': Number(location.latitude), 'lng': Number(location.longitude)};
const location_ep_id = location.ep_id;

// Don't want to have an Info box, this will be in a separate window on the right side
// filter based on location_ep_id
$.get('/episodes.json', (episodes) => {
  for (const episode of episodes) {
    // Define the content of the infoWindow
        <ul class="episode-info">
          <li><b>Season</b>${Episode.season}</li>
          <li><b>Episode Number</b>${Episode.episode_number}</li>
          <li><b>Doctor</b>${Episode.doctor}</li>
          <li><b>Title</b>${Episode.title}</li>
          <li><b>IMDB Link</b>${Episode.imdb}</li>
        </ul>

let map;

function initMap() {
    const map = new google.maps.Map(document.getElementById('#single_map'), {
      center: {
        latLng },
      zoom: 10,
    });
    const locationMarker = new google.maps.Marker({
      position: latLng,
      location_ep_id: location_ep_id,
      map: map,
      icon: {
              url: "/static/img/tardis.png",
              size:new google.maps.Size(20, 34)}
  });
          const locationMarker = new google.maps.Marker({
            position: {
              lat: Location.latitude,
              lng: Location.longitude
            },
            map: map,
          });
        }
