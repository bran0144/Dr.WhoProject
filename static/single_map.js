"use strict";


// need to get user selected data (probably just location_id) so we know which pins to
// send and what api call should be
// do we call api before rendering map? then send that data through initMap?
// Build a separate/permanent info box on single pin map instead of pop-up?
function initMap() {
    const map = new google.maps.Map($('#single_map')[0], {
      center: {
        lat: 51.509865,
        lng: -0.118092
      },
      scrollwheel: false,
      zoom: 5,
      zoomControl: true,
      panControl: false,
      streetViewControl: false,
    //   styles: MAPSTYLES,  // mapStyles is defined in mapstyles.js
      mapTypeId: google.maps.MapTypeId.TERRAIN
    });
  

    $.get('/locations.json', (locations) => {
        for (const location of locations) {
          // Define the content of the infoWindow
          const locationInfoContent = (
              <ul class="location-info">
                <li><b>Season</b>${Episode.season}</li>
                <li><b>Episode Number</b>${Episode.episode_number}</li>
                <li><b>Doctor</b>${Episode.doctor}</li>
                <li><b>Title</b>${Episode.title}</li>
                <li><b>IMDB Link</b>${Episode.imdb}</li>
                <li><b>Address</b>${Location.address}</li>
              </ul>
          );
    
          const locationMarker = new google.maps.Marker({
            position: {
              lat: Location.latitude,
              lng: Location.longitude
            },
            map: map,
          });
    
          locationMarker.addListener('click', () => {
            locationInfo.close();
            locationInfo.setContent(locationInfoContent);
            locationInfo.open(map, locationMarker);
          });
        }
      }).fail(() => {
        alert((`
         There are no pins matching your search.
        `));
      });
    }

