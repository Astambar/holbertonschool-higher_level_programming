#!/usr/bin/node
/*
fonction qui renvoie la version inversée d'une liste
*/
exports.esrever = function (list) {
  const output = [];

  while (list.length) {
    output.push(list.pop());
  }

  return output;
};
