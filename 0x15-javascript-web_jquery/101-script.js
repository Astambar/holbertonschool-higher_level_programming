#!/usr/bin/node
/*
Script qui permet d'ajouter des élément <li>Item</li> avec la commande:
add_item
permet aussi de suprimer le dernière élément générer avec remove_item
et de supprimer tout les  items avec clear_list
*/

const $JQ = window.$;
document.addEventListener('DOMContentLoaded', () => {
  $JQ('#add_item').click( () => {
    $JQ('UL.my_list').append('<li>Item</li>');
  });
  $JQ('#remove_item').click( () => {
    $('li:last-child').remove();
  });
  $JQ('#clear_list').click( () => {
    $JQ('li').remove();
  });
});
