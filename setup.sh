#!/bin/bash

./download_input.py
if [[ "$?" -eq 0 ]]
then
  v {year}/src/aoc{}.py
fi
