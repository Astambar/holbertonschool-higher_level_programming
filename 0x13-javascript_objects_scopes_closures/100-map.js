#!/usr/bin/node
/*
script qui importe un tableau et calcule un nouveau tableau
*/
const list = require('./100-data.js').list;
const mapList = [];

list.map((element, idx) => { return mapList.push(element * idx); });

console.log(list);
console.log(mapList);
