#!/usr/bin/node
/*
JavaScript script that fetches and lists the title for all movies
by using this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
*/
// const $ = window.$;
const $JQ = window.$;
$JQ(document).ready(() => {
  $JQ.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
    for (const movie in data.results) {
      $JQ('#list_movies').append('<li>' + data.results[movie].title + '</li>');
    }
  });
});
