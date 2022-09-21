#!/usr/bin/node
/*
JavaScript script that fetches and prints how to say “Hello”
depending on the language
*/
import fetch from 'node-fetch';

const $JQ = window.$;

document.addEventListener('DOMContentLoaded', () => {
  $JQ('#btn_translate').click(function () {
    fetch('https://www.fourtonfish.com/hellosalut/?lang=' + $JQ('#language_code').val())
      .then((response) => {
        return response.json();
      })
      .then((dataJsonFile) => {
        $JQ('#hello').text(dataJsonFile.hello);
      });
  });
});
