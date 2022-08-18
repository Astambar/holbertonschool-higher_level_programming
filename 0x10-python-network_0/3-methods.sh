#!/bin/bash
#script qui prend une URL et affiche toutes les méthodes HTTP que le serveur acceptera
curl -sI "$1" | grep "Allow: " | cut -d' ' -f 2-
