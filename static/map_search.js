"use strict";


let map;

function initMap() {
  map = new google.maps.Map(document.getElementById('searched_map'), {
    center: { lat: 51.509865, lng: -0.118092 },
    zoom: 5,
  });

  locations.forEach(location => {
    const address = location.address;
    const latLng = {'lat': Number(location.latitude), 'lng': Number(location.longitude)};
    const location_ep_id = location.ep_id;
    const location_id = location.location_id;
    
    const locationMarker = new google.maps.Marker({
        position: latLng,
        location_ep_id: location_ep_id,
        location_id: location_id,
        map: map,
        icon: {
                url: "/static/img/tardis.png",
                size:new google.maps.Size(20, 34)}
    });
    const locationInfo = new google.maps.InfoWindow();
      $.get('/episodes.json', (episodes => {
        for (const episode of episodes) {
         
          const ep_id = episode.ep_id;
          locationMarker.get('location_ep_id');
          const locationInfoContent = (
          <div class="window-content">
              <ul class="location-info">
                <li><b>Season</b>${episode.season}</li>
                <li><b>Episode Number</b>${episode.episode_number}</li>
                <li><b>Title</b>${episode.title}</li>
                <li><b>Doctor</b>${episode.doctor}</li>
                <li><b>Companion</b>{episode.companion}</li>
                <li><b>IMDB Link</b>${episode.imdb}</li>
              </ul>
          </div>
          ); 
          // TODO: need to connect info box ep_id to marker ep_id
          locationMarker.addEventListener('mouseover', () => {
            locationInfo.close();
            locationInfo.setContent(locationInfoContent);
            locationInfo.open(map, locationMarker);
          });
        }
      )}
 

  };
} 

