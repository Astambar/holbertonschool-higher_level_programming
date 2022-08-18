#!/bin/bash
#script qui prend une URL en argument, envoie un GET et affiche le corps 
curl -s "$1" -X GET -H "X-School-User-Id: 98"
