#!/bin/bash
#script qui prend une URL en argument, envoie un GET et affiche le corps 
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
