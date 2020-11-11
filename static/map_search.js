"use strict";
// need to get user selected data (probably just location_id) so we know which pins to
// send and what api call should be
// do we call api before rendering map? then send that data through initMap?

const LatLngObject = {lat: 0, lng:0};

function initMap() {
  $.get('/locations.json', (data) => {
    const response = JSON.parse(data);
    latLngObject['latitude'] = response.film_locations.latitude;
    latLngObject['longitude'] = response.film_locations.longitude;
    const searched_map = new.google.maps.Map(
      document.querySelector('#searched_map'),
      {
        center: latLngObject,
        zoom: 9,
      });
    const locationMarker = new google.maps.Marker({
      position: {
        lat: Location.latitude,
        lng: Location.longitude
    },
        map: searched_map,
          });
  })
}







// function initMap() {
//     const map = new google.maps.Map($('#searched_map')[0], {
//       center: {
//         lat: 51.509865,
//         lng: -0.118092
//       },
//       zoom: 5,

//     //   styles: MAPSTYLES,  // mapStyles is defined in mapstyles.js
//       mapTypeId: "terrain",
//     });

//     const locationInfo = new google.maps.InfoWindow();

//     $.get('/locations.json', (locations) => {
//         for (const location of locations) {
          // Define the content of the infoWindow
          // const locationInfoContent = (`
          // <div class="window-content">
          // // <div class="tardis-thumbnail">
          // //   <img
          // //     src="/static/img/tardis.jpg"
          // //     alt="tardis"
          // //   />
          // // </div>

          //     <ul class="location-info">
          //       <li><b>Season</b>${Episode.season}</li>
          //       <li><b>Episode Number</b>${Episode.episode_number}</li>
          //       <li><b>Doctor</b>${Episode.doctor}</li>
          //       <li><b>Title</b>${Episode.title}</li>
          //       <li><b>Address</b>${Location.address}</li>
          //     </ul>
          // `);
    
          // const locationMarker = new google.maps.Marker({
          //   position: {
          //     lat: Location.latitude,
          //     lng: Location.longitude
          //   },
          //   map: map,
          // });
    
          // locationMarker.addListener('click', () => {
          //   locationInfo.close();
          //   locationInfo.setContent(locationInfoContent);
          //   locationInfo.open(map, locationMarker);
    //       // });
    //     }
    //   }).fail(() => {
    //     alert((`
    //      There are no pins matching your search.
    //     `));
    //   });
    // }
