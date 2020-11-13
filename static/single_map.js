"use strict";


// Build a separate/permanent info box on single pin map (2nd sprint)

function initMap() {
    const map = new google.maps.Map(document.getElementById('#single_map') {
      center: {
        lat: 51.509865,
        lng: -0.118092
      },

      zoom: 5,
  
    //   styles: MAPSTYLES,  // mapStyles is defined in mapstyles.js
      mapTypeId: google.maps.MapTypeId.TERRAIN
    });
  

    $.get('/episodes.json', (episodes) => {
        for (const episode of episodes) {
          // Define the content of the infoWindow
          const locationInfoContent = (
              <ul class="location-info">
                <li><b>Season</b>${Episode.season}</li>
                <li><b>Episode Number</b>${Episode.episode_number}</li>
                <li><b>Doctor</b>${Episode.doctor}</li>
                <li><b>Title</b>${Episode.title}</li>
                <li><b>IMDB Link</b>${Episode.imdb}</li>
              </ul>
          );
    
          const locationMarker = new google.maps.Marker({
            position: {
              lat: Location.latitude,
              lng: Location.longitude
            },
            map: map,
          });
    
          locationMarker.addEventListener('mouseover', () => {
            locationInfo.close();
            locationInfo.setContent(locationInfoContent);
            locationInfo.open(map, locationMarker);
          });
        }
      });
    

