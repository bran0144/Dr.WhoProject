"use strict";

// const seasonButton = document.querySelector("#search-season-episode");

// $('#search-season-episode').on('click', (evt) => {
//     const formInputs = {
//         'season': $('#season').val(),
//         'episode_number': $('#episode-number').val()
//     };
//     $.get('/map_search', formInputs, (res) => {})
// });
// directs values from dropdowns to route
// @app.route('/map_search/<season>/<episode_number>')
// def create_map_from_season_search():

const seasonValues = $('#search-season-episode').serialize();

$.get('/map_search/<season>/<episode_number>', seasonValues, resultHandler);

// jquery and AJAX take form from dropdown menu of season and episode
// send to 'map_search' route



// const doctorButton = document.querySelector("#search-doctor");

// doctorButton.addEventListener('click', (evt) => {

// // directs value from downdown to route
// // @app.route('/map_search/<doctor>')
// // def create_map_from_doctor_search():
// });

const doctorValues = $('#search-doctor');

$.get('/map_search/<doctor>', doctorValues, resultHandler);

// jquery and AJAX take form from dropdown menu of doctor
// send to 'map_search' route


// const searchForm = document.querySelector("#episode-title");

// searchForm.addEventListener('submit', (evt) => {

// // directs value from text fiels to route
// // @app.route('/map_search')
// // def create_map_from_title_search():
// });

const titleValues = $('#episode-title');

$.get('/map_search/<title>', titleValues, resultHandler);

// jquery and AJAX take form from text box and
// send to 'map_search' route