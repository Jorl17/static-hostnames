#!/bin/bash
if [ -z "$1" ]
  then
	PREFIX=/usr/bin
  else
	PREFIX=$1
fi
cp static-hostnames.py static-hostnames $PREFIX
chmod +x $PREFIX/static-hostnames 
