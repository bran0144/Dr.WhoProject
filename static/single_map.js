"use strict";

let map;

function initMap() {
  const tardis = "/static/img/tardis-thumbnail.png"; 
  const location_ep_id = single_location.ep_id;
  const address = single_location.address;
  const latLng = {'lat': Number(single_location.latitude), 'lng': Number(single_location.longitude)};
 
  
    const map = new google.maps.Map(document.getElementById("map_canvas"), {
      center: latLng,
      zoom: 12,
    });

    const locationMarker = new google.maps.Marker({
        position: latLng,
        map: map,
        location_ep_id: location_ep_id,
        icon: tardis,
    });

}


