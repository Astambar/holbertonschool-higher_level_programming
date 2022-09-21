#!/usr/bin/node
/*
JavaScript script that adds, removes and clears LI elements
from a list when the user clicks
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
