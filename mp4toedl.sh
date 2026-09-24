#!/bin/sh
for file in *.mp4;
do
    mkedl.py "$file"
done
