#!/bin/bash
#Créer des requêtes curl qui envoient un fichier Json
curl -sX POST -H "Content-Type: application/json" --data @"$2" "$1"
