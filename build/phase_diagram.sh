#!/bin/sh
make clean 
make
rm ../result/*

echo "1"
./run true old 100 0.01 10
echo "2"
./run true old 100 0.01 10
