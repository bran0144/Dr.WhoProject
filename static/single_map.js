"use strict";


// Build a separate/permanent info box on single pin map (2nd sprint)

const address = single_location.address;
console.log(single_location.latitude);
console.log(single_location.longitude);
const latLng = {'lat': Number(single_location.latitude), 'lng': Number(single_location.longitude)};
console.log(latLng)
const location_ep_id = single_location.ep_id;

// Don't want to have an Info box, this will be in a separate window on the right side
// filter based on location_ep_id
// or just get all info by location_id from route call into Jinja
// $.get('/episodes.json', (episodes) => {
//   for (const episode of episodes) {
//     // Define the content of the infoWindow
//         <ul class="episode-info">
//           <li><b>Season</b>${Episode.season}</li>
//           <li><b>Episode Number</b>${Episode.episode_number}</li>
//           <li><b>Doctor</b>${Episode.doctor}</li>
//           <li><b>Title</b>${Episode.title}</li>
//           <li><b>IMDB Link</b>${Episode.imdb}</li>
//         </ul>

let map;

function initMap() {
    const map = new google.maps.Map(document.getElementById('single-map'), {
      center: latLng,
      zoom: 10,
    });
    const tardis = "/static/img/tardis-thumbnail.png";
    const locationMarker = new google.maps.Marker({
      position: latLng,
      location_ep_id: location_ep_id,
      map: map,
      icon: tardis,
  });
}

