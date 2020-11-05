"use strict";

function initMap() {
    const map = new google.maps.Map($('#searched_map')[0], {
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
  

    $.get('/api/locations', (locations) => {
        for (const location of locations) {
          // Define the content of the infoWindow
          const locationInfoContent = (`
            
    
              <ul class="location-info">
                <li><b>Season</b>${Episode.season}</li>
                <li><b>Episode Number</b>${Episode.episode_number}</li>
                <li><b>Doctor</b>${Episode.doctor}</li>
                <li><b>Title</b>${Episode.title}</li>
                <li><b>Address</b>${Location.address}</li>
              </ul>
            </div>
          `);
    
          const locationMarker = new google.maps.Marker({
            position: {
              lat: Location.latitude,
              lng: Location.longitude
            },
            // title: `Bear ID: ${bear.bearId}`,
            // icon: {
            //   url: '/static/img/polarBear.svg',
            //   scaledSize: new google.maps.Size(50, 50)
            // },
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
          We were unable to retrieve data about bears :(
    
          Did you remember to create the bears database and seed it?
          (See model.py and seed.py for more info).
        `));
      });

// // load data using the map.data.loadGeoJson() method. data needs to be in a json format

// // Loop through the results array and place a marker for each
// // set of coordinates.
// const eqfeed_callback = function (results) {
//   for (let i = 0; i < results.features.length; i++) {
//     const coords = results.features[i].geometry.coordinates;
//     const latLng = new google.maps.LatLng(coords[1], coords[0]);
//     new google.maps.Marker({
//       position: latLng,
//       map: map,
//     });
//   }
// };