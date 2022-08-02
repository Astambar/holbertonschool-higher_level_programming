#!/usr/bin/node
/*
fonction qui convertit un nombre en base 10
à une autre base passée en argument
*/
exports.converter = function (base) {
  return function (nb) {
    return nb.toString(base);
  };
};
