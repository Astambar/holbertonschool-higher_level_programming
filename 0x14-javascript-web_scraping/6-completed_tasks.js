#!/usr/bin/node
/*
gets the contents of a webpage and stores it in a file
*/

const axios = require('axios');

axios({
  method: 'get',
  url: process.argv[2]
})
  .then((response) => {
    const dictionaryTask = {};
    let val;
    const data = response.data;
    for ([, val] of Object.entries(data)) {
      if (val.completed === true) {
        if (dictionaryTask[val.userId] === undefined) {
			dictionaryTask[val.userId] = 0;
        }
        dictionaryTask[val.userId] += 1;
      }
    }
    console.log(dictionaryTask);
  }, (error) => {
    console.log('code : ' + error.response.status);
  });
