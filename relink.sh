#!/bin/bash

LNKDIR='/home/will/Programs/mathing/path'

for FILE in ./*.py
do
	NAME="${FILE%.*}"
	ln -sv $FILE $LNKDIR/$NAME
	chmod +x $LNKDIR/$NAME
done
