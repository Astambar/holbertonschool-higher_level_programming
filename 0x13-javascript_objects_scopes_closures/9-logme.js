#!/usr/bin/node
/*
fonction qui imprime le nombre d'arguments
déjà imprimé et la nouvelle valeur d'argument
*/
exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count += 1;
};

let count = 0;
