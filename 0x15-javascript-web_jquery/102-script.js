#!/usr/bin/node
/*
Script JavaScript qui récupère et imprime comment dire "Bonjour"
selon la langue
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
