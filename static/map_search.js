"use strict";

function setupMouseOver(map, locationMarker, location_ep_id) {
  $.get('/api/episodes/' + location_ep_id, function(episodeInfo){
      locationInfoContent = (`
          <div class="window-content">
              <ul class="episode-info">
                <li><b>Season:</b>  ${episodeInfo.season}</li>
                <li><b>Episode Number:</b>  ${episodeInfo.episode_number}</li>
                <li><b>Title:</b>  ${episodeInfo.title}</li>
                <li><b>Doctor:</b>  ${episodeInfo.doctor}</li>
                <li><b>Companion:</b>  ${episodeInfo.companion}</li>
                <li><b>Guest Star:</b>  ${episodeInfo.guest_star}</li>
                
              </ul>
          </div>
          `); 
   
    console.log(episodeInfo);
    const infoWindow = new google.maps.InfoWindow({
      content: locationInfoContent,
      maxWidth: 300,
    });
    locationMarker.addListener('mouseover', () => {
        infoWindow.open(map, locationMarker);
          });
    locationMarker.addListener('mouseout', () => {
        infoWindow.close(map, locationMarker);
          });
    }); 
  }

let map;

function initMap() {
  const map = new google.maps.Map(document.getElementById("searched_map"), {
    center: { lat: 51.509865, lng: -0.118092 },
    zoom: 5,
  });

  locations.forEach(location => {
    const address = location.address;
    const latLng = {'lat': Number(location.latitude), 'lng': Number(location.longitude)};
    const location_ep_id = location.ep_id;
    const location_id = location.location_id;
    const tardis = "/static/img/tardis-thumbnail.png";
    
    
    const locationMarker = new google.maps.Marker({
        position: latLng,
        map: map,
        icon: tardis,
        location_ep_id: location_ep_id,
        location_id: location_id,        
        url: "/single_map/" + location_id,
    });
   setupMouseOver(map, locationMarker, location_ep_id); 
    

    locationMarker.addListener('click', () => {
        window.location.href = locationMarker.url;
          });
}); 
  } 

