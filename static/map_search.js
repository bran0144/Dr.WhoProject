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
  

    $.get('/api/bears', (bears) => {
        for (const bear of bears) {
          // Define the content of the infoWindow
          const bearInfoContent = (`
            <div class="window-content">
              <div class="bear-thumbnail">
                <img
                  src="/static/img/polarbear.jpg"
                  alt="polarbear"
                />
              </div>
    
              <ul class="bear-info">
                <li><b>Bear gender: </b>${bear.gender}</li>
                <li><b>Bear birth year: </b>${bear.birthYear}</li>
                <li><b>Year captured: </b>${bear.capYear}</li>
                <li><b>Collared: </b>${bear.collared}</li>
                <li><b>Location: </b>${bear.capLat}, ${bear.capLong}</li>
              </ul>
            </div>
          `);
    
          const bearMarker = new google.maps.Marker({
            position: {
              lat: bear.capLat,
              lng: bear.capLong
            },
            title: `Bear ID: ${bear.bearId}`,
            icon: {
              url: '/static/img/polarBear.svg',
              scaledSize: new google.maps.Size(50, 50)
            },
            map: map,
          });
    
          bearMarker.addListener('click', () => {
            bearInfo.close();
            bearInfo.setContent(bearInfoContent);
            bearInfo.open(map, bearMarker);
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