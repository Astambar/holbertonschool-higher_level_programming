#!/bin/bash
#Créer une requête curl avec des données dans le header
curl -s -o /dev/null -w "%{http_code}" "$1"
