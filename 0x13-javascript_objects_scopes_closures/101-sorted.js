#!/usr/bin/node
/*
script qui importe un dictionnaire d'occurrences par identifiant d'utilisateur
et calcule un dictionnaire d'identifiants d'utilisateurs par occurrence
*/
const dict = require('./101-data.js').dict;
const newDict = {};

for (const [key, value] of Object.entries(dict)) {
  if (!newDict[value]) { newDict[value] = []; }
  newDict[value].push(key);
}

console.log(newDict);
