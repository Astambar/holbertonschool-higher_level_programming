#!/usr/bin/env bash
# -*- coding: utf-8 -*-
tab=(
	'./2-args.py'
	'./2-args.py Hello'
	)

for (( i=0;${tab[i]} -eq null ; i++ ))
do
  echo ${tab[i]}
done

