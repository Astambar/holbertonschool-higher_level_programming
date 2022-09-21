#!/usr/bin/node
/*
Script qui affiche la valeur de hello de l'url: https://fourtonfish.com/hellosalut/?lang=fr
 dans l'id nommé hello
*/
const $JQ = window.$;
$JQ(document).ready(() => {
  $JQ.get('https://fourtonfish.com/hellosalut/?lang=fr',(dataHellosalut) => {
    $JQ('#hello').append(dataHellosalut.hello);
  });
});
