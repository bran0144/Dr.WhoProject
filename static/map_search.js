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




//     const locationInfo = new google.maps.InfoWindow();

//     $.get('/episodes.json', (episodes => {
//         for (const episode of episodes) {
         
          // const locationInfoContent = (`
          // <div class="window-content">
          // // <div class="tardis-thumbnail">
          // //   <img
          // //     src="/static/img/tardis.png"
          // //     alt="tardis"
          // //   />
          // // </div>

          //     <ul class="location-info">
          //       <li><b>Season</b>${Episode.season}</li>
          //       <li><b>Episode Number</b>${Episode.episode_number}</li>
          //       <li><b>Doctor</b>${Episode.doctor}</li>
          //       <li><b>Title</b>${Episode.title}</li>
          //       <li><b>IMDB Link</b>${Episode.imdb}</li>
          //     </ul>
          // `);
    
    
          // locationMarker.addEventListener('mouseover', () => {
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
 
    // this should work on click to take you to route , but how to send location_id
    //  .on event delegation - takes one or more events
    // .on('click', [selector] [data], handler)
    // can use $.ajax - can set converters (will convert json to jquery parseJson)
    // data, method = GET, or PUT?, url (where request is sent), 
    // could do XMLHttpRequest

    