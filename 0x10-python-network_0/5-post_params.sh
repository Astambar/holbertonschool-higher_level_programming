#!/bin/bash
#script qui prend une URL, envoie un POST et affiche le corps de la réponse
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
