#!/usr/bin/node
/*
prints the number of movies
where the character “Wedge Antilles” is present (id 18)
*/

const axios = require('axios');

axios.get(process.argv[2])
  .then(response => {
    let count = 0;
    for (const film of response.data.results) {
      for (const character of film.characters) {
        if (character.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
  )
  .catch(err => console.log(err));
