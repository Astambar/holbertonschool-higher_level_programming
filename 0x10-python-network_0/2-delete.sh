#!/bin/bash
#script qui envoie une requête DELETE à l'URL transmise et affiche le corps de la réponse
curl -s "$1" -X DELETE
