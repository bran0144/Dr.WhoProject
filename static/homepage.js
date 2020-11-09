"use strict";

const seasonButton = document.querySelector("#search-season-episode");

$('#search-season-episode').on('click', (evt) => {
    const formInputs = {
        'season': $('#season').val(),
        'episode_number': $('#episode-number').val()
    };
    $.get('/map_search', formInputs, (res) => {})
});


// const seasonValues = $('#search-season-episode').serialize();

// $.get('/map_search', seasonValues, resultHandler);

// jquery and AJAX take form from dropdown menu of season and episode
// send to 'map_search' route


const doctorButton = document.querySelector("#search-doctor");

$('#search-doctor').on('click', (evt) => {
    const formInputs = {
        'doctor': $('doctor').val()
    };
    $.get('map_search', formInputs, (res) => {})
});

// doctorButton.addEventListener('click', (evt) => {



// const doctorValues = $('#search-doctor').serialize();

// $.get('/map_search', doctorValues, resultHandler);

// jquery and AJAX take form from dropdown menu of doctor
// send to 'map_search' route

const searchForm = document.querySelector("#episode-title");

$('#episode-title').on('click', (evt) => {
    const formInputs = {
        'title': $('title').val()
    };
    $.get('map_search', formInputs, (res) => {})
});

// searchForm.addEventListener('submit', (evt) => {

// // directs value from text fiels to route
// // @app.route('/map_search')
// // def create_map_from_title_search():
// });

// const titleValues = $('#episode-title').serialize();

// $.get('/map_search', titleValues, resultHandler);

// jquery and AJAX take form from text box and
// send to 'map_search' route