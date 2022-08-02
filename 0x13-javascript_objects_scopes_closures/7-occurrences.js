#!/usr/bin/node
/*
fonction qui renvoie le nombre d'occurrences dans une liste
*/
exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (let i = 0; list[i]; i++) {
    if (list[i] === searchElement) { count += 1; }
  }

  return count;
};
